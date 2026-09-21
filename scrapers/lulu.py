import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from core.normalizer import parse_quantity


LULU_URL = (
    "https://gcc.luluhypermarket.com/"
    "en-bh/Online-Exclusive/c/CPBHN0101"
)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/131.0 Safari/537.36"
    )
}


def extract_price(text):

    if not text:
        return None

    match = re.search(
        r"(\d+(?:\.\d+)?)\s*BHD",
        text
    )

    if not match:
        return None

    return float(match.group(1))


def get_lulu_products():

    response = requests.get(
        LULU_URL,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    products = []

    # LuLu pages can change their HTML structure.
    # We deliberately keep the parser defensive.
    for element in soup.find_all(
        string=re.compile(r"BHD", re.I)
    ):

        price_text = element.parent.get_text(
            " ",
            strip=True
        )

        price = extract_price(price_text)

        if price is None:
            continue

        container = element.parent

        for _ in range(5):

            if not container:
                break

            text = container.get_text(
                " ",
                strip=True
            )

            if len(text) > 30:

                if "BHD" in text:

                    products.append({
                        "raw_text": text,
                        "price": price
                    })

                    break

            container = container.parent

    # Remove duplicates
    unique = []
    seen = set()

    for product in products:

        key = (
            product["raw_text"],
            product["price"]
        )

        if key not in seen:

            seen.add(key)
            unique.append(product)

    return unique


def classify_product(name):

    name_lower = name.lower()

    if any(
        word in name_lower
        for word in ["chicken", "tender", "griller"]
    ):
        return "Chicken"

    if any(
        word in name_lower
        for word in ["water", "drinking water"]
    ):
        return "Water"

    if any(
        word in name_lower
        for word in ["milk"]
    ):
        return "Milk"

    if any(
        word in name_lower
        for word in ["rice"]
    ):
        return "Rice"

    if any(
        word in name_lower
        for word in ["egg", "eggs"]
    ):
        return "Eggs"

    if any(
        word in name_lower
        for word in [
            "detergent",
            "soap",
            "cleaner",
            "bleach"
        ]
    ):
        return "Cleaning"

    return "Other"


def collect_lulu():

    raw_products = get_lulu_products()

    results = []

    for item in raw_products:

        text = item["raw_text"]

        price = item["price"]

        # Try to identify an original price.
        prices = re.findall(
            r"(\d+(?:\.\d+)?)\s*BHD",
            text
        )

        original_price = None

        if len(prices) >= 2:

            possible_original = float(prices[1])

            if possible_original > price:
                original_price = possible_original

        # Product name is approximated from the text.
        # The parser can be refined for LuLu's exact HTML.
        name = text

        quantity, unit = parse_quantity(
            text
        )

        results.append({
            "product_name": name,
            "category": classify_product(name),
            "store": "LuLu",
            "price": price,
            "original_price": original_price,
            "quantity": quantity,
            "unit": unit,
            "pack_description": None,
            "source_url": LULU_URL,
            "collected_at": datetime.now().isoformat(
                timespec="seconds"
            )
        })

    return results
