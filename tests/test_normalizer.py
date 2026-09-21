from core.normalizer import parse_quantity


def test_water_pack():

    quantity, unit = parse_quantity(
        "6 x 1.5L"
    )

    assert quantity == 9
    assert unit == "L"


def test_millilitre_pack():

    quantity, unit = parse_quantity(
        "12 x 500ml"
    )

    assert quantity == 6
    assert unit == "L"


def test_kg():

    quantity, unit = parse_quantity(
        "5kg"
    )

    assert quantity == 5
    assert unit == "kg"


def test_grams():

    quantity, unit = parse_quantity(
        "400g"
    )

    assert quantity == 0.4
    assert unit == "kg"
