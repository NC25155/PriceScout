from datetime import datetime


def demo_products():

    now = datetime.now().isoformat(
        timespec="seconds"
    )

    return [

        {
            "product_name": "Tanmiah Fresh Whole Chicken",
            "category": "Chicken",
            "store": "LuLu",
            "price": 1.625,
            "original_price": 1.825,
            "quantity": 1,
            "unit": "kg",
            "pack_description": "1 kg",
            "source_url": "https://gcc.luluhypermarket.com/",
            "collected_at": now
        },

        {
            "product_name": "Fresh Whole Chicken",
            "category": "Chicken",
            "store": "Demo Store",
            "price": 1.750,
            "original_price": None,
            "quantity": 1,
            "unit": "kg",
            "pack_description": "1 kg",
            "source_url": "",
            "collected_at": now
        },

        {
            "product_name": "LuLu Bottled Drinking Water",
            "category": "Water",
            "store": "LuLu",
            "price": 0.690,
            "original_price": None,
            "quantity": 6,
            "unit": "L",
            "pack_description": "12 x 500 ml",
            "source_url": "https://gcc.luluhypermarket.com/",
            "collected_at": now
        },

        {
            "product_name": "Bottled Drinking Water",
            "category": "Water",
            "store": "Demo Store",
            "price": 0.650,
            "original_price": 0.750,
            "quantity": 7.2,
            "unit": "L",
            "pack_description": "12 x 600 ml",
            "source_url": "",
            "collected_at": now
        },

        {
            "product_name": "Fresh Milk",
            "category": "Milk",
            "store": "LuLu",
            "price": 1.250,
            "original_price": 1.450,
            "quantity": 2,
            "unit": "L",
            "pack_description": "2 L",
            "source_url": "https://gcc.luluhypermarket.com/",
            "collected_at": now
        },

        {
            "product_name": "Long Life Milk",
            "category": "Milk",
            "store": "Demo Store",
            "price": 1.350,
            "original_price": None,
            "quantity": 2,
            "unit": "L",
            "pack_description": "2 L",
            "source_url": "",
            "collected_at": now
        }
    ]
