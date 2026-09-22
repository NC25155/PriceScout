from datetime import datetime


# NOTE: These are illustrative starter values, not live-scraped prices.
# Every entry links to a real, currently-operating Bahrain grocery
# storefront so you can click through and check the live price yourself.
# Swap this out for real collector output (see scrapers/lulu.py) once a
# working per-store scraper is confirmed for each chain.

LULU_URL = "https://gcc.luluhypermarket.com/en-bh/Online-Exclusive/c/CPBHN0101"
ALOSRA_URL = "https://www.talabat.com/bahrain/grocery/50392/alosra-aljuffair"
HYPERMAX_URL = "https://www.talabat.com/bahrain/grocery/711604/hypermax-riffa-alshamali-north-riffa"
AL_JAZIRA_URL = "https://www.talabat.com/bahrain/grocery/727495/al-jazira-supermarket-hamala"
TALAL_URL = "https://www.talabat.com/bahrain/grocery/718139/talal-markets-arad-new"


def demo_products():

    now = datetime.now().isoformat(
        timespec="seconds"
    )

    raw = [

        # ---------------- Chicken ----------------
        ("Tanmiah Fresh Whole Chicken", "Chicken", "LuLu", 1.625, 1.825, 1, "kg", "1 kg", LULU_URL),
        ("Fresh Whole Chicken", "Chicken", "Alosra", 1.750, None, 1, "kg", "1 kg", ALOSRA_URL),
        ("Fresh Whole Chicken", "Chicken", "HyperMax", 1.690, 1.890, 1, "kg", "1 kg", HYPERMAX_URL),
        ("Chicken Breast Fillet", "Chicken", "LuLu", 2.450, None, 1, "kg", "1 kg", LULU_URL),
        ("Chicken Breast Fillet", "Chicken", "HyperMax", 2.390, None, 1, "kg", "1 kg", HYPERMAX_URL),
        ("Chicken Drumsticks", "Chicken", "Al Jazira", 1.590, None, 1, "kg", "1 kg", AL_JAZIRA_URL),

        # ---------------- Meat & Seafood ----------------
        ("Fresh Beef Cubes", "Meat & Seafood", "LuLu", 3.450, 3.950, 1, "kg", "1 kg", LULU_URL),
        ("Fresh Lamb Chops", "Meat & Seafood", "Al Jazira", 5.250, None, 1, "kg", "1 kg", AL_JAZIRA_URL),
        ("Fresh Hammour Fish", "Meat & Seafood", "HyperMax", 4.990, None, 1, "kg", "1 kg", HYPERMAX_URL),
        ("Frozen Shrimp, Medium", "Meat & Seafood", "Alosra", 3.690, 4.190, 1, "kg", "1 kg", ALOSRA_URL),

        # ---------------- Water ----------------
        ("LuLu Bottled Drinking Water", "Water", "LuLu", 0.690, None, 6, "L", "12 x 500 ml", LULU_URL),
        ("Bottled Drinking Water", "Water", "Alosra", 0.650, 0.750, 7.2, "L", "12 x 600 ml", ALOSRA_URL),
        ("Bottled Drinking Water", "Water", "HyperMax", 0.700, None, 9, "L", "6 x 1.5 L", HYPERMAX_URL),
        ("Natural Mineral Water", "Water", "Talal Markets", 1.150, None, 6, "L", "6 x 1 L", TALAL_URL),

        # ---------------- Milk ----------------
        ("Fresh Milk", "Milk", "LuLu", 1.250, 1.450, 2, "L", "2 L", LULU_URL),
        ("Long Life Milk", "Milk", "Alosra", 1.350, None, 2, "L", "2 L", ALOSRA_URL),
        ("Fresh Milk", "Milk", "HyperMax", 1.290, None, 2, "L", "2 L", HYPERMAX_URL),
        ("Low Fat Milk", "Milk", "Al Jazira", 1.190, None, 2, "L", "2 L", AL_JAZIRA_URL),

        # ---------------- Dairy & Cheese ----------------
        ("Natural Yoghurt", "Dairy & Cheese", "LuLu", 0.750, None, 1, "kg", "1 kg tub", LULU_URL),
        ("Cheddar Cheese Slices", "Dairy & Cheese", "Alosra", 1.590, 1.890, 0.2, "kg", "200 g", ALOSRA_URL),
        ("Halloumi Cheese", "Dairy & Cheese", "Al Jazira", 2.290, None, 0.5, "kg", "500 g", AL_JAZIRA_URL),
        ("Labneh", "Dairy & Cheese", "HyperMax", 0.890, None, 0.4, "kg", "400 g", HYPERMAX_URL),

        # ---------------- Rice ----------------
        ("Basmati Rice", "Rice", "LuLu", 3.950, 4.450, 5, "kg", "5 kg", LULU_URL),
        ("Basmati Rice", "Rice", "Alosra", 4.100, None, 5, "kg", "5 kg", ALOSRA_URL),
        ("Basmati Rice", "Rice", "HyperMax", 3.890, None, 5, "kg", "5 kg", HYPERMAX_URL),
        ("Egyptian Rice", "Rice", "Al Jazira", 2.450, None, 5, "kg", "5 kg", AL_JAZIRA_URL),

        # ---------------- Eggs ----------------
        ("Bahraini Brown Eggs, Large", "Eggs", "Alosra", 2.690, None, 30, "pcs", "30 pieces", ALOSRA_URL),
        ("Fresh White Eggs, Large", "Eggs", "LuLu", 2.450, 2.750, 30, "pcs", "30 pieces", LULU_URL),
        ("Farm Fresh Eggs, Medium", "Eggs", "HyperMax", 2.290, None, 30, "pcs", "30 pieces", HYPERMAX_URL),
        ("Omega-3 Eggs, 15 pieces", "Eggs", "Al Jazira", 4.350, None, 15, "pcs", "15 pieces", AL_JAZIRA_URL),

        # ---------------- Cleaning ----------------
        ("Laundry Detergent Powder", "Cleaning", "LuLu", 2.995, 3.495, 3, "kg", "3 kg", LULU_URL),
        ("Laundry Detergent Powder", "Cleaning", "Alosra", 3.150, None, 3, "kg", "3 kg", ALOSRA_URL),
        ("Multi-Surface Cleaner", "Cleaning", "HyperMax", 1.190, 1.390, 1.5, "L", "1.5 L", HYPERMAX_URL),
        ("Dishwashing Liquid", "Cleaning", "Talal Markets", 0.790, None, 1, "L", "1 L", TALAL_URL),

        # ---------------- Bakery ----------------
        ("Sliced White Bread", "Bakery", "LuLu", 0.395, None, 1, "loaf", "600 g loaf", LULU_URL),
        ("Sliced Brown Bread", "Bakery", "Alosra", 0.450, None, 1, "loaf", "600 g loaf", ALOSRA_URL),
        ("Arabic Pita Bread", "Bakery", "HyperMax", 0.290, None, 1, "pack", "10 pieces", HYPERMAX_URL),
        ("Croissants", "Bakery", "Al Jazira", 0.990, None, 1, "pack", "6 pieces", AL_JAZIRA_URL),

        # ---------------- Cooking Oil ----------------
        ("Sunflower Oil", "Cooking Oil", "LuLu", 2.250, 2.550, 1.8, "L", "1.8 L", LULU_URL),
        ("Sunflower Oil", "Cooking Oil", "Alosra", 2.390, None, 1.8, "L", "1.8 L", ALOSRA_URL),
        ("Olive Oil Extra Virgin", "Cooking Oil", "HyperMax", 3.950, 4.450, 1, "L", "1 L", HYPERMAX_URL),
        ("Corn Oil", "Cooking Oil", "Talal Markets", 1.990, None, 1.5, "L", "1.5 L", TALAL_URL),

        # ---------------- Fruits & Vegetables ----------------
        ("Fresh Bananas", "Fruits & Vegetables", "LuLu", 0.650, None, 1, "kg", "1 kg", LULU_URL),
        ("Fresh Tomatoes", "Fruits & Vegetables", "Alosra", 0.590, None, 1, "kg", "1 kg", ALOSRA_URL),
        ("Fresh Potatoes", "Fruits & Vegetables", "HyperMax", 0.450, None, 1, "kg", "1 kg", HYPERMAX_URL),
        ("Fresh Cucumbers", "Fruits & Vegetables", "HyperMax", 0.390, 0.490, 1, "kg", "1 kg", HYPERMAX_URL),
        ("Fresh Oranges", "Fruits & Vegetables", "Al Jazira", 0.750, None, 1, "kg", "1 kg", AL_JAZIRA_URL),
        ("Red Onions", "Fruits & Vegetables", "Talal Markets", 0.390, None, 1, "kg", "1 kg", TALAL_URL),

        # ---------------- Dates & Dried Fruit ----------------
        ("Bahraini Khalas Dates", "Dates & Dried Fruit", "Al Jazira", 2.950, None, 1, "kg", "1 kg", AL_JAZIRA_URL),
        ("Mixed Dried Fruit", "Dates & Dried Fruit", "LuLu", 2.450, 2.850, 0.5, "kg", "500 g", LULU_URL),
        ("Medjool Dates", "Dates & Dried Fruit", "Alosra", 3.990, None, 1, "kg", "1 kg", ALOSRA_URL),

        # ---------------- Snacks ----------------
        ("Potato Chips Family Pack", "Snacks", "LuLu", 1.450, 1.750, 1, "pack", "6 x 40 g", LULU_URL),
        ("Mixed Nuts", "Snacks", "Alosra", 2.990, None, 0.5, "kg", "500 g", ALOSRA_URL),
        ("Chocolate Biscuits", "Snacks", "HyperMax", 0.850, None, 1, "pack", "300 g", HYPERMAX_URL),
        ("Popcorn", "Snacks", "Talal Markets", 0.590, None, 1, "pack", "150 g", TALAL_URL),

        # ---------------- Frozen Food ----------------
        ("Frozen French Fries", "Frozen Food", "LuLu", 1.190, 1.390, 1, "kg", "1 kg", LULU_URL),
        ("Frozen Mixed Vegetables", "Frozen Food", "Alosra", 0.990, None, 1, "kg", "1 kg", ALOSRA_URL),
        ("Frozen Chicken Nuggets", "Frozen Food", "HyperMax", 1.590, None, 0.5, "kg", "500 g", HYPERMAX_URL),
        ("Frozen Paratha", "Frozen Food", "Al Jazira", 0.990, None, 1, "pack", "10 pieces", AL_JAZIRA_URL),

        # ---------------- Beverages ----------------
        ("Cola Soft Drink", "Beverages", "LuLu", 2.250, None, 1.5, "L", "6 x 250 ml cans", LULU_URL),
        ("Orange Juice", "Beverages", "Alosra", 1.150, 1.350, 1, "L", "1 L", ALOSRA_URL),
        ("Energy Drink", "Beverages", "HyperMax", 0.550, None, 1, "can", "250 ml", HYPERMAX_URL),
        ("Laban", "Beverages", "Talal Markets", 0.450, None, 1, "L", "1 L", TALAL_URL),

        # ---------------- Coffee & Tea ----------------
        ("Instant Coffee", "Coffee & Tea", "LuLu", 3.450, 3.950, 0.2, "kg", "200 g", LULU_URL),
        ("Ceylon Tea Bags", "Coffee & Tea", "Al Jazira", 1.590, None, 1, "pack", "100 bags", AL_JAZIRA_URL),
        ("Arabic Coffee", "Coffee & Tea", "Alosra", 2.290, None, 0.25, "kg", "250 g", ALOSRA_URL),

        # ---------------- Canned Goods ----------------
        ("Canned Tuna in Oil", "Canned Goods", "LuLu", 0.550, None, 1, "can", "185 g", LULU_URL),
        ("Canned Chickpeas", "Canned Goods", "HyperMax", 0.390, None, 1, "can", "400 g", HYPERMAX_URL),
        ("Canned Tomato Paste", "Canned Goods", "Talal Markets", 0.290, None, 1, "can", "400 g", TALAL_URL),

        # ---------------- Pasta & Noodles ----------------
        ("Spaghetti Pasta", "Pasta & Noodles", "LuLu", 0.450, None, 0.5, "kg", "500 g", LULU_URL),
        ("Instant Noodles Multipack", "Pasta & Noodles", "Alosra", 1.290, None, 1, "pack", "5 x 75 g", ALOSRA_URL),
        ("Penne Pasta", "Pasta & Noodles", "HyperMax", 0.490, None, 0.5, "kg", "500 g", HYPERMAX_URL),

        # ---------------- Spices & Condiments ----------------
        ("Mixed Spice Blend", "Spices & Condiments", "Al Jazira", 0.990, None, 0.2, "kg", "200 g", AL_JAZIRA_URL),
        ("Tomato Ketchup", "Spices & Condiments", "LuLu", 0.850, 0.990, 0.5, "kg", "500 g", LULU_URL),
        ("Mayonnaise", "Spices & Condiments", "HyperMax", 1.150, None, 0.5, "kg", "500 g", HYPERMAX_URL),

        # ---------------- Personal Care ----------------
        ("Shampoo", "Personal Care", "LuLu", 2.750, 3.250, 0.4, "L", "400 ml", LULU_URL),
        ("Toothpaste", "Personal Care", "Alosra", 1.190, None, 0.1, "kg", "100 g", ALOSRA_URL),
        ("Hand Soap", "Personal Care", "HyperMax", 0.990, None, 0.5, "L", "500 ml", HYPERMAX_URL),
        ("Tissue Paper Box", "Personal Care", "Talal Markets", 0.590, None, 1, "box", "200 sheets", TALAL_URL),
    ]

    return [
        {
            "product_name": name,
            "category": category,
            "store": store,
            "price": price,
            "original_price": original_price,
            "quantity": quantity,
            "unit": unit,
            "pack_description": pack_description,
            "source_url": source_url,
            "collected_at": now
        }
        for (
            name, category, store, price, original_price,
            quantity, unit, pack_description, source_url
        ) in raw
    ]
