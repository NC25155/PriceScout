import re


def normalize_text(value: str) -> str:
    if not value:
        return ""

    value = value.lower()
    value = value.replace("×", "x")
    value = value.replace(" litre", "l")
    value = value.replace(" litres", "l")
    value = value.replace(" liter", "l")
    value = value.replace(" liters", "l")

    return value.strip()


def parse_quantity(text: str):
    """
    Examples:

        6 x 1.5L  -> 9.0 L
        12 x 500ml -> 6.0 L
        1 kg -> 1.0 kg
        400 g -> 0.4 kg
        2 L -> 2.0 L
    """

    if not text:
        return None, None

    text = normalize_text(text)

    # 6 x 1.5L
    multi = re.search(
        r"(\d+(?:\.\d+)?)\s*x\s*(\d+(?:\.\d+)?)\s*(ml|l|g|kg)",
        text
    )

    if multi:
        count = float(multi.group(1))
        amount = float(multi.group(2))
        unit = multi.group(3)

        total = count * amount

        if unit == "ml":
            total /= 1000
            unit = "L"

        elif unit == "g":
            total /= 1000
            unit = "kg"

        elif unit == "l":
            unit = "L"

        return total, unit

    # 1.5L / 500ml / 1kg / 400g
    single = re.search(
        r"(\d+(?:\.\d+)?)\s*(ml|l|g|kg)",
        text
    )

    if single:
        amount = float(single.group(1))
        unit = single.group(2)

        if unit == "ml":
            amount /= 1000
            unit = "L"

        elif unit == "g":
            amount /= 1000
            unit = "kg"

        elif unit == "l":
            unit = "L"

        return amount, unit

    return None, None


def calculate_unit_price(price, quantity, unit):
    if price is None or quantity is None or quantity == 0:
        return None

    return round(price / quantity, 3)


def format_unit_price(value, unit):
    if value is None:
        return "N/A"

    return f"{value:.3f} BHD/{unit}"
