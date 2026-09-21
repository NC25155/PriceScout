from core.comparator import (
    calculate_discount,
    compare_products
)


def test_discount():

    result = calculate_discount(
        8,
        10
    )

    assert result == 20


def test_price_comparison():

    products = [
        {
            "product_name": "A",
            "price": 2,
            "quantity": 1,
            "unit": "kg"
        },
        {
            "product_name": "B",
            "price": 1,
            "quantity": 1,
            "unit": "kg"
        }
    ]

    results = compare_products(
        products,
        "unit_price"
    )

    assert results[0]["product_name"] == "B"
