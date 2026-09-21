def calculate_discount(price, original_price):
    if not original_price:
        return None

    if original_price <= 0:
        return None

    if price >= original_price:
        return 0.0

    return round(
        ((original_price - price) / original_price) * 100,
        1
    )


def compare_products(products, criterion="unit_price"):
    """
    Sort products according to a user-selected criterion.

    Supported:
        total_price
        unit_price
        discount
    """

    results = []

    for product in products:

        item = product.copy()

        quantity = item.get("quantity")
        unit = item.get("unit")
        price = item.get("price")

        if quantity and unit:
            item["unit_price"] = round(
                price / quantity,
                3
            )
        else:
            item["unit_price"] = None

        item["discount"] = calculate_discount(
            price,
            item.get("original_price")
        )

        results.append(item)

    if criterion == "discount":
        results.sort(
            key=lambda x: x["discount"] or 0,
            reverse=True
        )

    elif criterion == "total_price":
        results.sort(
            key=lambda x: x["price"]
        )

    else:
        results.sort(
            key=lambda x: (
                x["unit_price"]
                if x["unit_price"] is not None
                else float("inf")
            )
        )

    return results
