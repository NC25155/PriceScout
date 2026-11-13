"""Retailer catalogue snapshots checked on 13 November 2026.

These are source-backed listing observations, not fabricated demo prices.
Retailers can change prices or stock at any time; each row links to its source.
"""
from datetime import date

CHECKED = "2026-11-13"
LULU_RICE = "https://gcc.luluhypermarket.com/en-bh/grocery-food-cupboard-rice-pasta-noodles-rice/"
LULU_SAVERS = "https://gcc.luluhypermarket.com/en-bh/lulu-savers/c/CPBHN98"
LULU_EXCLUSIVE = "https://gcc.luluhypermarket.com/en-bh/Online-Exclusive/c/CPBHN037/"
HYPERMAX_FLOUR = "https://www.hypermax.com.bh/mafbhr/en/c/50931"
STORE_TO_DOOR_RICE = "https://storetodoor.bh/product-category/grocery/"

# name, category, store, BHD, original BHD, quantity, unit, pack, source URL
ROWS = [
    # Rice: compare cost per kg, while keeping rice varieties visible.
    ("LuLu US Style Parboiled Rice", "Rice", "LuLu", 4.190, None, 10, "kg", "10 kg", "https://gcc.luluhypermarket.com/en-bh/lulu-us-style-parboiled-rice-10-kg/p/495456"),
    ("LuLu White Rice", "Rice", "LuLu", 2.190, None, 5, "kg", "5 kg", LULU_RICE),
    ("LuLu US Style Parboiled Rice", "Rice", "LuLu", 2.190, None, 5, "kg", "5 kg", LULU_RICE),
    ("LuLu White Raw Rice", "Rice", "LuLu", 2.390, None, 5, "kg", "5 kg", LULU_EXCLUSIVE),
    ("LuLu Long Grain Matta Rice", "Rice", "LuLu", 2.990, None, 5, "kg", "5 kg", LULU_RICE),
    ("Sunwhite Calrose Rice", "Rice", "LuLu", 7.780, None, 10, "kg", "10 kg", LULU_RICE),
    ("Brahmins Long Grain Matta Rice", "Rice", "LuLu", 7.190, None, 10, "kg", "10 kg", LULU_RICE),
    ("LuLu Thai US Style Rice", "Rice", "LuLu", 0.990, None, 2, "kg", "2 kg", LULU_RICE),
    ("LuLu White Rice", "Rice", "LuLu", 1.190, None, 2, "kg", "2 kg", LULU_RICE),
    ("Abu Shaiba Basmati Rice", "Rice", "Store To Door", 13.500, None, 20, "kg", "20 kg", STORE_TO_DOOR_RICE),
    ("Fakhar Basmati Rice Aromatic", "Rice", "Store To Door", 13.900, None, 20, "kg", "20 kg", STORE_TO_DOOR_RICE),
    ("Mohsen Basmati Rice", "Rice", "Store To Door", 13.500, None, 20, "kg", "20 kg", STORE_TO_DOOR_RICE),
    ("Olive Basmati Rice", "Rice", "Store To Door", 13.500, None, 20, "kg", "20 kg", STORE_TO_DOOR_RICE),
    ("Kashmir Indian Basmati Rice", "Rice", "Store To Door", 14.400, None, 20, "kg", "20 kg", STORE_TO_DOOR_RICE),

    # Other Bahrain retailers and comparison sites: bulk 18–20 kg options.
    ("Sindbad Pakistani White Rice", "Rice", "Order Maza", 9.000, None, 20, "kg", "20 kg", "https://ordermaza.com/shop?category=rice"),
    ("Prawn Premium Basmati Rice", "Rice", "Shefs", 9.490, None, 20, "kg", "20 kg", "https://www.shef-s.com/collections/rice"),
    ("Chakra Andhra Korthula Rice", "Rice", "Shefs", 5.990, None, 18, "kg", "18 kg", "https://www.shef-s.com/collections/rice"),
    ("Jawaher Basmati Rice", "Rice", "Order Maza", 10.500, None, 20, "kg", "20 kg", "https://ordermaza.com/shop?category=rice"),
    ("Al Habib Basmati Rice", "Rice", "Ansar Gallery", 10.950, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Maryam Indian Sella Basmati Rice", "Rice", "Ansar Gallery", 10.775, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Jabbal Long Grain Punjab Basmati Rice", "Rice", "Ansar Gallery", 11.075, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Kashmir Indian Basmati Rice", "Rice", "Ansar Gallery", 12.925, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Fakhar Indian Basmati Rice", "Rice", "Ansar Gallery", 12.650, 14.450, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Mohsen 21 Basmati Rice", "Rice", "Ansar Gallery", 13.995, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Mohsen Basmati 1121 Sella Rice", "Rice", "Ansar Gallery", 11.550, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Banno Basmati Rice", "Rice", "Ansar Gallery", 14.195, None, 20, "kg", "20 kg", "https://www.ansargallery.bh/en/grocery/dry-food/rice?p=2"),
    ("Ruman Basmati Rice", "Rice", "Shefs", 11.490, None, 20, "kg", "20 kg", "https://www.shef-s.com/collections/rice"),
    ("Al Malik 1121 Indian Premium Basmati Rice", "Rice", "Shefs", 11.960, None, 20, "kg", "20 kg", "https://www.shef-s.com/collections/rice"),
    ("Indian Harvest Basmati Rice Value Pack", "Rice", "Shefs", 11.000, None, 20, "kg", "20 kg", "https://www.shef-s.com/collections/rice"),
    ("Rumanain Indian Basmati Rice", "Rice", "Lotus Food", 11.550, None, 20, "kg", "20 kg", "https://lotusbh.odoo.com/shop/category/cooking-products-rice-grains-510"),
    ("Al Khairat Steam Rice", "Rice", "Lotus Food", 11.550, None, 20, "kg", "20 kg", "https://lotusbh.odoo.com/shop/category/cooking-products-rice-grains-510"),
    ("Zaina Sella Bukhary Basmati Rice", "Rice", "Order Maza", 11.500, None, 20, "kg", "20 kg", "https://ordermaza.com/shop?category=rice"),
    ("Royal Queen Classic Basmati Rice", "Rice", "Order Maza", 12.000, None, 20, "kg", "20 kg", "https://ordermaza.com/shop?category=rice"),
    ("Maza Bukhary Extra Basmati Rice", "Rice", "Order Maza", 12.000, None, 20, "kg", "20 kg", "https://ordermaza.com/shop?category=rice"),
    ("Maza Basmati Rice XL", "Rice", "Order Maza", 12.600, None, 20, "kg", "20 kg", "https://ordermaza.com/shop?category=rice"),

    # Retailer-published hot deals: discount percentages are shown explicitly
    # by Order Maza even when the previous price is not provided in the listing.
    ("MAZA Tomato Ketchup", "Spices & Condiments", "Order Maza", 0.720, None, 0.55, "kg", "550 g", "https://ordermaza.com/"),
    ("MAZA All Purpose Wheat Flour", "Flour & Baking", "Order Maza", 0.495, None, 1, "kg", "1 kg", "https://ordermaza.com/"),
    ("MAZA Soft Tissues Deluxe", "Paper & Tissue", "Order Maza", 1.350, None, 750, "sheets", "5 x 150 sheets", "https://ordermaza.com/"),
    ("MAZA White Crystal Sugar", "Sugar", "Order Maza", 0.810, None, 2, "kg", "2 kg", "https://ordermaza.com/"),
    ("MAZA White Crystal Sugar", "Sugar", "Order Maza", 3.510, None, 10, "kg", "10 kg", "https://ordermaza.com/"),
    ("MAZA Sunflower Oil", "Cooking Oil", "Order Maza", 2.755, None, 2, "L", "2 L", "https://ordermaza.com/"),


    # Flour, sugar and cooking oil.
    ("Al Matahin All Purpose Flour", "Flour & Baking", "HyperMax", 0.580, None, 2, "kg", "2 kg", HYPERMAX_FLOUR),
    ("Al Matahin All Purpose Flour", "Flour & Baking", "HyperMax", 0.310, None, 1, "kg", "1 kg", HYPERMAX_FLOUR),
    ("Al Osra Fine Sugar", "Sugar", "LuLu", 3.450, None, 10, "kg", "10 kg", LULU_SAVERS),
    ("Al Osra Fine Sugar", "Sugar", "LuLu", 2.300, None, 5, "kg", "5 kg", LULU_EXCLUSIVE),
    ("LuLu Sunflower Oil", "Cooking Oil", "LuLu", 5.290, None, 5, "L", "5 L", LULU_EXCLUSIVE),
    ("Noor Sunflower Oil Value Pack", "Cooking Oil", "LuLu", 3.490, None, 3, "L", "2 x 1.5 L", LULU_SAVERS),

    # Monthly household essentials and cleaning.
    ("Persil Automatic Washing Powder Green", "Laundry", "LuLu", 3.390, 3.590, 5, "kg", "5 kg", LULU_SAVERS),
    ("Persil Power Gel Liquid Detergent", "Laundry", "LuLu", 5.290, None, 4.8, "L", "4.8 L", LULU_SAVERS),
    ("Ariel Platinum Gel Liquid Detergent", "Laundry", "LuLu", 4.990, None, 4, "L", "4 L", LULU_SAVERS),
    ("Comfort Fabric Softener Spring Dew", "Laundry", "LuLu", 1.845, None, 2.9, "L", "2.9 L", LULU_SAVERS),
    ("LuLu Antiseptic Disinfectant", "Cleaning", "LuLu", 1.980, None, 1, "L", "2 x 500 ml", LULU_SAVERS),
    ("Windex Glass Cleaner Value Pack", "Cleaning", "LuLu", 2.770, None, 1.5, "L", "2 x 750 ml", LULU_SAVERS),
    ("Kleenex Daily Care Facial Tissue", "Paper & Tissue", "LuLu", 1.295, 2.590, 850, "sheets", "5 x 170 sheets", LULU_SAVERS),
    ("Kleenex Extra Dry Toilet Tissue", "Paper & Tissue", "LuLu", 3.500, None, 12, "rolls", "9 + 3 rolls", LULU_SAVERS),
    ("Kleenex Dry Soft Toilet Tissue", "Paper & Tissue", "LuLu", 5.140, None, 20, "rolls", "16 + 4 rolls", LULU_SAVERS),
    ("LuLu Softouch Facial Tissue", "Paper & Tissue", "LuLu", 1.945, None, 1000, "sheets", "5 x 200 sheets", LULU_EXCLUSIVE),

    # Regular food basket.
    ("LuLu White Eggs Large", "Eggs", "LuLu", 2.000, None, 30, "pcs", "30 pieces", LULU_SAVERS),
    ("Bahrain Fresh White Eggs Large", "Eggs", "LuLu", 2.160, None, 30, "pcs", "30 pieces", LULU_EXCLUSIVE),
    ("Al Safi UHT Full Fat Milk", "Milk & Dairy", "LuLu", 1.750, None, 4, "L", "4 x 1 L", LULU_SAVERS),
    ("LuLu Frozen Chicken Breast", "Chicken", "LuLu", 4.110, None, 2, "kg", "2 kg", LULU_EXCLUSIVE),
    ("Tanmiah Fresh Whole Chicken", "Chicken", "LuLu", 1.630, 1.825, 1, "kg", "1 kg", LULU_EXCLUSIVE),
    ("Al Ain French Fries", "Frozen Food", "LuLu", 2.255, None, 2, "kg", "2 kg", LULU_EXCLUSIVE),
    ("LuLu White Oats", "Breakfast", "LuLu", 1.635, None, 1, "kg", "1 kg", LULU_EXCLUSIVE),
    ("Al Ain Tomato Paste Value Pack", "Canned Goods", "LuLu", 1.225, None, 1.08, "kg", "8 x 135 g", LULU_EXCLUSIVE),
    ("Puck Cheese Triangles", "Milk & Dairy", "LuLu", 0.720, None, 0.24, "kg", "240 g", LULU_EXCLUSIVE),
    ("Tomato", "Fruits & Vegetables", "LuLu", 0.330, None, 0.5, "kg", "500 g", LULU_EXCLUSIVE),
    ("Cucumber", "Fruits & Vegetables", "LuLu", 0.135, None, 0.5, "kg", "500 g", LULU_EXCLUSIVE),
]

def demo_products():
    """Return source-backed retailer snapshot rows for the app's catalogue."""
    products = [{
        "product_name": name,
        "category": category,
        "store": store,
        "city": "All Bahrain",
        "price": price,
        "original_price": original,
        "quantity": quantity,
        "unit": unit,
        "pack_description": pack,
        "source_url": url,
        "collected_at": CHECKED,
        "checked_at": CHECKED,
        "data_status": "Retailer listing snapshot — confirm stock and final checkout price",
    } for name, category, store, price, original, quantity, unit, pack, url in ROWS]

    published_deals = {
        ("MAZA Tomato Ketchup", "Order Maza"): 10,
        ("MAZA All Purpose Wheat Flour", "Order Maza"): 10,
        ("MAZA Soft Tissues Deluxe", "Order Maza"): 10,
        ("MAZA White Crystal Sugar", "Order Maza"): 10,
        ("MAZA Sunflower Oil", "Order Maza"): 5,
        ("Maza Basmati Rice XL", "Order Maza"): 10,
    }
    for item in products:
        deal = published_deals.get((item["product_name"], item["store"]))
        if deal is not None:
            item["discount_percent"] = deal
    return products
