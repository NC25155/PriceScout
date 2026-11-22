
"""LuLu Bahrain public catalogue scraper.

Diagnostic version: reports what the LuLu website returns
so scraping problems can be identified without inventing prices.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from core.normalizer import parse_quantity


BASE_URL = "https://gcc.luluhypermarket.com"
LIST_URL = f"{BASE_URL}/en-bh/list/"
MAX_PAGES = 5
PAGE_SIZE = 50
TIMEOUT = 25

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0 Safari/537.36"
    ),
    "Accept": "application/json, text/html;q=0.9, */*;q=0.8",
    "Accept-Language": "en-BH,en;q=0.9",
    "Referer": f"{BASE_URL}/en-bh/",
}


def _number(value):
    """Convert a price-like value to float."""
    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, dict):
        for key in ("value", "amount", "price"):
            if key in value:
                result = _number(value[key])
                if result is not None:
                    return result

    if isinstance(value, str):
        cleaned = value.replace(",", "")
        match = re.search(r"\d+(?:\.\d{1,3})?", cleaned)

        if match:
            try:
                return float(match.group(0))
            except ValueError:
                return None

    return None


def _get_price(product):
    """Read prices from common catalogue formats."""
    for key in (
        "price",
        "selling_price",
        "sale_price",
        "discounted_price",
        "final_price",
    ):
        value = product.get(key)

        if value is not None:
            price = _number(value)

            if price is not None:
                return price

    for key in ("pricing", "prices", "price_details"):
        nested = product.get(key)

        if isinstance(nested, dict):
            for price_key in (
                "price",
                "selling_price",
                "sale_price",
                "current",
                "value",
                "amount",
            ):
                price = _number(nested.get(price_key))

                if price is not None:
                    return price

    return None


def _get_currency(product):
    """Find currency information in common catalogue formats."""
    for key in ("currency_type", "currency", "currency_code"):
        value = product.get(key)

        if isinstance(value, dict):
            value = (
                value.get("code")
                or value.get("name")
                or value.get("symbol")
            )

        if value:
            return str(value).strip().upper()

    for key in ("pricing", "prices", "price_details"):
        nested = product.get(key)

        if isinstance(nested, dict):
            for currency_key in (
                "currency",
                "currency_code",
                "currency_type",
            ):
                value = nested.get(currency_key)

                if isinstance(value, dict):
                    value = (
                        value.get("code")
                        or value.get("name")
                        or value.get("symbol")
                    )

                if value:
                    return str(value).strip().upper()

    return ""


def _get_name(product):
    """Find product names from common fields."""
    for key in (
        "name",
        "title",
        "product_name",
        "display_name",
        "description",
    ):
        value = product.get(key)

        if isinstance(value, str) and value.strip():
            return value.strip()

    return None


def _get_url(product):
    """Find a product URL."""
    for key in ("absolute_url", "url", "product_url", "slug"):
        value = product.get(key)

        if isinstance(value, str) and value.strip():
            if key == "slug":
                return urljoin(LIST_URL, value)

            return urljoin(BASE_URL, value)

    return LIST_URL


def _product_from_object(obj):
    """Convert one JSON object into a normalized product."""
    if not isinstance(obj, dict):
        return None

    product = obj.get("product")

    if not isinstance(product, dict):
        product = obj

    name = _get_name(product)
    price = _get_price(product)
    currency = _get_currency(product)

    if not name or price is None or price <= 0:
        return None

    # Accept only explicitly identified Bahraini currency.
    if currency not in {"BHD", "BD", "د.ب", "BH"}:
        return None

    retail = None

    for key in (
        "retail_price",
        "original_price",
        "list_price",
        "old_price",
    ):
        retail = _number(product.get(key))

        if retail is not None:
            break

    if retail is not None and retail <= price:
        retail = None

    quantity, unit = parse_quantity(str(name))

    return {
        "product_name": re.sub(r"\s+", " ", str(name)).strip(),
        "category": classify_product(str(name)),
        "store": "LuLu",
        "price": price,
        "original_price": retail,
        "quantity": quantity,
        "unit": unit,
        "pack_description": None,
        "source_url": _get_url(product),
        "collected_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        ),
    }


def _walk_products(value):
    """Recursively find product-shaped objects in JSON."""
    results = []

    if isinstance(value, dict):
        normalized = _product_from_object(value)

        if normalized:
            results.append(normalized)
        else:
            for child in value.values():
                results.extend(_walk_products(child))

    elif isinstance(value, list):
        for child in value:
            results.extend(_walk_products(child))

    return results


def _json_listing(session, page):
    """Fetch one JSON catalogue page and print diagnostic details."""
    params = {
        "format": "json",
        "page": page,
        "limit": PAGE_SIZE,
    }

    try:
        response = session.get(
            LIST_URL,
            params=params,
            timeout=TIMEOUT,
        )

        print(f"LuLu URL: {response.url}")
        print(f"LuLu status: {response.status_code}")
        print(
            "LuLu content type: "
            f"{response.headers.get('Content-Type')}"
        )
        print(
            "LuLu response preview: "
            f"{response.text[:1000]}"
        )

        response.raise_for_status()

        try:
            payload = response.json()
        except ValueError:
            print("WARNING: LuLu did not return valid JSON.")
            return None

        if isinstance(payload, dict):
            print(f"LuLu JSON keys: {list(payload.keys())}")

        sample_products = _walk_products(payload)

        print(
            f"Products recognized on page {page}: "
            f"{len(sample_products)}"
        )

        return payload

    except requests.RequestException as error:
        print(f"LuLu request failed: {error}")
        return None


def _html_listing(session):
    """Fallback parser for product cards and JSON-LD."""
    try:
        response = session.get(
            LIST_URL,
            timeout=TIMEOUT,
        )

        print(f"LuLu HTML status: {response.status_code}")
        print(
            "LuLu HTML content type: "
            f"{response.headers.get('Content-Type')}"
        )

        response.raise_for_status()

    except requests.RequestException as error:
        print(f"LuLu HTML request failed: {error}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    print(
        "LuLu HTML page title: "
        f"{soup.title.get_text(strip=True) if soup.title else 'No title'}"
    )

    results = []

    for script in soup.select(
        'script[type="application/ld+json"]'
    ):
        try:
            data = json.loads(
                script.string or script.get_text()
            )
            results.extend(_walk_products(data))

        except (ValueError, TypeError):
            continue

    selectors = [
        "[data-product]",
        ".product-card",
        ".product-item",
        ".product",
        "article",
    ]

    for selector in selectors:
        for card in soup.select(selector):
            text = card.get_text(" ", strip=True)

            price_match = re.search(
                r"(\d+(?:\.\d{1,3})?)\s*"
                r"(?:BHD|BD|د\.ب)",
                text,
                flags=re.IGNORECASE,
            )

            if not price_match:
                continue

            name_node = card.select_one(
                "[data-product-name], .product-name, "
                ".product__name, .name, h2, h3, [title]"
            )

            name = ""

            if name_node:
                name = (
                    name_node.get("data-product-name")
                    or name_node.get("title")
                    or name_node.get_text(" ", strip=True)
                )

            if not name:
                image_node = card.select_one("img[alt]")

                name = (
                    image_node.get("alt", "")
                    if image_node
                    else ""
                )

            if not name:
                continue

            price = float(price_match.group(1))

            old_price_node = card.select_one(
                ".old-price, .price-old, .was-price, "
                ".product-price-old, [data-old-price], del, s"
            )

            old_price = None

            if old_price_node:
                old_text = (
                    old_price_node.get("data-old-price")
                    or old_price_node.get_text(" ", strip=True)
                )

                old_price = _number(old_text)

                if old_price is not None and old_price <= price:
                    old_price = None

            quantity, unit = parse_quantity(name)

            link = card.select_one("a[href]")

            results.append({
                "product_name": re.sub(
                    r"\s+", " ", name
                ).strip(),
                "category": classify_product(name),
                "store": "LuLu",
                "price": price,
                "original_price": old_price,
                "quantity": quantity,
                "unit": unit,
                "pack_description": None,
                "source_url": (
                    urljoin(BASE_URL, link["href"])
                    if link
                    else LIST_URL
                ),
                "collected_at": datetime.now(
                    timezone.utc
                ).isoformat(timespec="seconds"),
            })

        if results:
            break

    unique = []
    seen = set()

    for product in results:
        key = (
            product["product_name"].casefold(),
            round(product["price"], 3),
        )

        if key not in seen:
            seen.add(key)
            unique.append(product)

    print(f"Products recognized in HTML: {len(unique)}")

    return unique


def extract_price(text):
    """Compatibility helper for other project modules."""
    if not text:
        return None

    match = re.search(
        r"(\d+(?:\.\d{1,3})?)\s*(?:BHD|BD)",
        text,
        re.I,
    )

    return float(match.group(1)) if match else None


def classify_product(name):
    """Assign a basic product category."""
    value = name.lower()

    groups = [
        ("Rice", ("rice", "basmati", "calrose", "matta")),
        ("Flour & Baking", ("flour", "semolina", "baking", "yeast")),
        ("Sugar", ("sugar",)),
        ("Cooking Oil", ("cooking oil", "sunflower oil", "corn oil", "vegetable oil", "olive oil")),
        ("Laundry", ("detergent", "washing powder", "fabric softener", "softener")),
        ("Paper & Tissue", ("tissue", "toilet roll", "toilet paper", "paper towel")),
        ("Cleaning", ("cleaner", "disinfectant", "bleach", "windex", "dishwash")),
        ("Personal Care", ("shampoo", "toothpaste", "soap", "deodorant")),
        ("Chicken", ("chicken", "tender", "nugget", "griller")),
        ("Eggs", ("egg",)),
        ("Milk & Dairy", ("milk", "cheese", "labneh", "yoghurt", "yogurt", "butter")),
        ("Frozen Food", ("frozen", "fries", "paratha")),
        ("Breakfast", ("oats", "cereal", "corn flakes")),
        ("Water", ("water",)),
        ("Canned Goods", ("canned", "tomato paste", "tuna", "chickpeas")),
        ("Fruits & Vegetables", ("tomato", "cucumber", "potato", "onion", "carrot", "apple", "banana")),
        ("Pasta & Noodles", ("pasta", "spaghetti", "noodles", "macaroni")),
    ]

    for category, words in groups:
        if any(word in value for word in words):
            return category

    return "Other"


def get_lulu_products():
    """Collect Bahrain catalogue products without fabricating prices."""
    session = requests.Session()
    session.headers.update(HEADERS)

    products = []
    seen = set()

    for page in range(1, MAX_PAGES + 1):
        payload = _json_listing(session, page)

        if payload is None:
            break

        page_products = _walk_products(payload)

        for item in page_products:
            key = (
                item["product_name"].casefold(),
                round(item["price"], 3),
            )

            if key not in seen:
                seen.add(key)
                products.append(item)

        if not page_products or len(page_products) < PAGE_SIZE:
            break

    if not products:
        print("Trying LuLu HTML fallback...")
        products = _html_listing(session)

    if not products:
        print(
            "WARNING: LuLu Bahrain could not be scraped. "
            "No prices were added for LuLu today."
        )
        return []

    print(f"Total valid LuLu products collected: {len(products)}")

    return products


def collect_lulu():
    """Compatibility function used by the daily collector."""
    return get_lulu_products()

