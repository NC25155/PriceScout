"""LuLu Bahrain public catalogue scraper.

Uses Akinon's documented public /list/?format=json storefront response
first, then falls back to structured HTML when JSON is unavailable.
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
    """Convert a price-like value to float without guessing currencies."""
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = re.search(r"\d+(?:[.,]\d{1,3})?", value.replace(",", ""))
        if match:
            return float(match.group(0).replace(",", "."))
    return None


def _product_from_object(obj):
    """Normalize one Akinon product or product-list wrapper."""
    if not isinstance(obj, dict):
        return None

    product = obj.get("product") if isinstance(obj.get("product"), dict) else obj
    name = product.get("name") or product.get("title") or product.get("product_name")
    raw_price = product.get("price") or product.get("selling_price") or product.get("sale_price")
    # Never assume a missing currency is BHD. The storefront can return
    # regional catalogue data; accepting an unlabelled number caused AED-like
    # values to be displayed as BHD.
    raw_currency = product.get("currency_type") or product.get("currency")
    currency = str(raw_currency).strip().upper() if raw_currency is not None else ""

    if not name or raw_price is None or not currency:
        return None
    if currency not in {"BHD", "BD", "د.ب", "BH"}:
        return None

    price = _number(raw_price)
    if price is None or price <= 0:
        return None

    retail = _number(
        product.get("retail_price")
        or product.get("original_price")
        or product.get("list_price")
    )
    if retail is not None and retail <= price:
        retail = None

    path = product.get("absolute_url") or product.get("url") or ""
    source_url = urljoin(BASE_URL, path) if path else LIST_URL
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
        "source_url": source_url,
        "collected_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def _walk_products(value):
    """Find product-shaped dictionaries in common Akinon JSON envelopes."""
    found = []
    if isinstance(value, dict):
        normalized = _product_from_object(value)
        if normalized:
            found.append(normalized)
            return found
        for child in value.values():
            found.extend(_walk_products(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_walk_products(child))
    return found


def _json_listing(session, page):
    params = {"format": "json", "page": page, "limit": PAGE_SIZE}
    response = session.get(LIST_URL, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    try:
        return response.json()
    except (ValueError, json.JSONDecodeError):
        return None


def _html_listing(session):
    """Fallback parser for product cards and Product JSON-LD."""
    response = session.get(LIST_URL, timeout=TIMEOUT)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for script in soup.select('script[type="application/ld+json"]'):
        try:
            results.extend(_walk_products(json.loads(script.string or script.get_text())))
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
                r"(\d+(?:\.\d{1,3})?)\s*(?:BHD|BD|د\.ب)",
                text,
                flags=re.IGNORECASE,
            )
            if not price_match:
                continue

            name_node = card.select_one(
                "[data-product-name], .product-name, .product__name, "
                ".name, h2, h3, [title]"
            )
            name = ""
            if name_node:
                name = (
                    name_node.get("data-product-name")
                    or name_node.get("title")
                    or name_node.get_text(" ", strip=True)
                )
            if not name:
                image = card.select_one("img[alt]")
                name = image.get("alt", "") if image else ""
            if not name:
                continue

            price = float(price_match.group(1))
            old_price_node = card.select_one(
                ".old-price, .price-old, .was-price, .product-price-old, "
                "[data-old-price], del, s"
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
                "product_name": re.sub(r"\s+", " ", name).strip(),
                "category": classify_product(name),
                "store": "LuLu",
                "price": price,
                "original_price": old_price,
                "quantity": quantity,
                "unit": unit,
                "pack_description": None,
                "source_url": urljoin(BASE_URL, link["href"]) if link else LIST_URL,
                "collected_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
        if results:
            break

    return results


def extract_price(text):
    """Compatibility helper retained for other project modules."""
    if not text:
        return None
    match = re.search(r"(\d+(?:\.\d{1,3})?)\s*(?:BHD|BD)", text, re.I)
    return float(match.group(1)) if match else None


def classify_product(name):
    value = name.lower()
    groups = {
        "Chicken": ("chicken", "tender", "nugget", "nuggets", "griller"),
        "Water": ("water",),
        "Milk": ("milk",),
        "Rice": ("rice",),
        "Eggs": ("egg", "eggs"),
        "Cleaning": ("detergent", "soap", "cleaner", "bleach"),
    }
    for category, words in groups.items():
        if any(word in value for word in words):
            return category
    return "Other"


def get_lulu_products():
    """Return de-duplicated live catalogue products from LuLu Bahrain."""
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
            key = (item["product_name"].casefold(), round(item["price"], 3))
            if key not in seen:
                seen.add(key)
                products.append(item)

        if not page_products or len(page_products) < PAGE_SIZE:
            break

    if not products:
        products = _html_listing(session)

    if not products:
        raise RuntimeError(
            "LuLu returned no parseable Bahrain products from /list/?format=json "
            "or the structured HTML fallback. The site may have changed or blocked "
            "automated requests; no sample prices were substituted."
        )
    return products


def collect_lulu():
    return get_lulu_products()
