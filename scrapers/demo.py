"""Retailer catalogue snapshots checked on 13 November 2026.

These are source-backed listing observations, not fabricated demo prices.
Retailers can change prices or stock at any time; each row links to its source.
"""
from datetime import date

CHECKED = "2026-11-13"
LULU_RICE = "https://gcc.luluhypermarket.com/en-bh/grocery-food-cupboard-rice-pasta-noodles-rice"
LULU_SAVERS = "https://gcc.luluhypermarket.com/en-bh/lulu-savers/c/CPBHN98"
LULU_EXCLUSIVE = "https://gcc.luluhypermarket.com/en-bh/Online-Exclusive/c/CPBHN037"
NASS_FOODS_HAMALA = "https://www.talabat.com/bahrain/grocery/646804/nassfoods-madinat-hamad-hamad-town?aid=1056"
LIVE_WELL_HAMALA = "https://www.talabat.com/bahrain/grocery/689325/marketplace-by-live-well-hamala?aid=1056"
AL_MARKAZI_HAMALA = "https://www.talabat.com/bahrain/grocery/620119/al-markazi-central-market-alnoaim?aid=1056"
HYPERMAX_FLOUR = "https://www.hypermax.com.bh/mafbhr/en/c/50931"
STORE_TO_DOOR_RICE = "https://storetodoor.bh/product-category/grocery/"

# name, category, store, BHD, original BHD, quantity, unit, pack, source URL
ROWS = [
    # Rice: compare cost per kg, while keeping rice varieties visible.
    ("LuLu US Style Parboiled Rice", "Rice", "LuLu", 4.190, None, 10, "kg", "10 kg", LULU_RICE),
    ("LuLu White Rice", "Rice", "LuLu", 2.190, None, 5, "kg", "5 kg", "https://gcc.luluhypermarket.com/en-bh/lulu-white-rice-5-kg/p/1494350/"),
    ("LuLu US Style Parboiled Rice", "Rice", "LuLu", 2.190, None, 5, "kg", "5 kg", LULU_RICE),
    ("LuLu White Raw Rice", "Rice", "LuLu", 2.390, None, 5, "kg", "5 kg", LULU_EXCLUSIVE),
    ("LuLu Long Grain Matta Rice", "Rice", "LuLu", 2.990, None, 5, "kg", "5 kg", LULU_RICE),
    ("Sunwhite Calrose Rice", "Rice", "LuLu", 7.780, None, 10, "kg", "10 kg", LULU_RICE),
    ("Brahmins Long Grain Matta Rice", "Rice", "LuLu", 7.190, None, 10, "kg", "10 kg", LULU_RICE),
    ("LuLu Thai US Style Rice", "Rice", "LuLu", 0.990, None, 2, "kg", "2 kg", LULU_RICE),
    ("LuLu White Rice", "Rice", "LuLu", 1.190, None, 2, "kg", "2 kg", "https://gcc.luluhypermarket.com/en-bh/lulu-white-rice-2-kg/p/1494349/"),
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



    # Hamala delivery listings from Talabat menus (area-specific catalogue snapshots).
    ("Aviko Mozzarella Fingers", "Frozen Food", "Nass Foods", 5.880, None, 1, "kg", "1 kg", NASS_FOODS_HAMALA),
    ("Mydibel Spicy Potato Wedges", "Frozen Food", "Nass Foods", 2.300, None, 2.5, "kg", "2.5 kg", NASS_FOODS_HAMALA),
    ("Gold Winner Sunflower Oil", "Cooking Oil", "Nass Foods", 1.634, None, 1.5, "L", "1.5 L", NASS_FOODS_HAMALA),
    ("Gold Winner Sunflower Oil", "Cooking Oil", "Nass Foods", 5.143, None, 5, "L", "5 L", NASS_FOODS_HAMALA),
    ("Sabrina Vegetable Oil", "Cooking Oil", "Nass Foods", 11.000, None, 18, "L", "18 L", NASS_FOODS_HAMALA),
    ("Mara Pomace Olive Oil", "Cooking Oil", "Nass Foods", 3.630, None, 1, "L", "1 L", NASS_FOODS_HAMALA),
    ("Mara Pomace Olive Oil", "Cooking Oil", "Nass Foods", 10.890, None, 4, "L", "4 L", NASS_FOODS_HAMALA),
    ("Forz Sunflower Oil", "Cooking Oil", "Nass Foods", 2.100, None, 1.8, "L", "1.8 L", NASS_FOODS_HAMALA),
    ("Duke's Corn Oil", "Cooking Oil", "Nass Foods", 2.800, None, 1.8, "L", "1.8 L", NASS_FOODS_HAMALA),
    ("Kitchen King Supreme Basmati Rice", "Rice", "Nass Foods", 15.150, None, 20, "kg", "20 kg", NASS_FOODS_HAMALA),
    ("Anarkali 1121 Steam Basmati Rice", "Rice", "Nass Foods", 14.170, None, 20, "kg", "20 kg", NASS_FOODS_HAMALA),
    ("Mara Red Kidney Beans", "Canned Goods", "Nass Foods", 0.320, None, 0.4, "kg", "400 g", NASS_FOODS_HAMALA),
    ("Mara Whole Peeled Tomatoes", "Canned Goods", "Nass Foods", 0.380, None, 0.4, "kg", "400 g", NASS_FOODS_HAMALA),
    ("Cold Alex Okra", "Frozen Food", "Nass Foods", 0.420, None, 0.8, "kg", "2 x 400 g", NASS_FOODS_HAMALA),
    ("Cold Alex Strawberries", "Frozen Food", "Nass Foods", 0.490, None, 0.4, "kg", "400 g", NASS_FOODS_HAMALA),

    ("Dr Schar Wafer Nocciole Hazelnut", "Snacks", "Live Well", 1.650, None, 0.125, "kg", "125 g", LIVE_WELL_HAMALA),
    ("Dr Schar Milly Gris And Ciocc", "Snacks", "Live Well", 1.630, None, 0.052, "kg", "52 g", LIVE_WELL_HAMALA),
    ("Dr Schar Snacks", "Snacks", "Live Well", 2.310, None, 0.105, "kg", "105 g", LIVE_WELL_HAMALA),
    ("Dr Schar Digestive Choc", "Snacks", "Live Well", 2.310, None, 0.15, "kg", "150 g", LIVE_WELL_HAMALA),
    ("Dr Schar Corn Flakes", "Breakfast", "Live Well", 2.260, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("Dr Schar Cereal Flakes", "Breakfast", "Live Well", 3.220, None, 0.3, "kg", "300 g", LIVE_WELL_HAMALA),
    ("Dr Schar Maria Biscuit", "Snacks", "Live Well", 1.630, None, 0.125, "kg", "125 g", LIVE_WELL_HAMALA),
    ("Dr Schar Chocolate Chip Cookie", "Snacks", "Live Well", 1.680, None, 0.1, "kg", "100 g", LIVE_WELL_HAMALA),
    ("Dr Schar Digestive Biscuits", "Snacks", "Live Well", 1.760, None, 0.15, "kg", "150 g", LIVE_WELL_HAMALA),
    ("Dr Schar Twin Bar", "Snacks", "Live Well", 1.860, None, 0.0645, "kg", "64.5 g", LIVE_WELL_HAMALA),
    ("Dr Schar Marble Cake", "Bakery", "Live Well", 3.360, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("Dr Schar Salti", "Snacks", "Live Well", 2.420, None, 0.175, "kg", "175 g", LIVE_WELL_HAMALA),
    ("Dr Schar Fette Croccanti Cracker Toast", "Snacks", "Live Well", 2.000, None, 0.15, "kg", "150 g", LIVE_WELL_HAMALA),
    ("Schar Chocolate O'S", "Snacks", "Live Well", 2.680, None, 0.165, "kg", "165 g", LIVE_WELL_HAMALA),
    ("Schar Sorrisi Biscuits", "Snacks", "Live Well", 2.360, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("DSC Ciocko Sticks", "Snacks", "Live Well", 2.940, None, 0.15, "kg", "150 g", LIVE_WELL_HAMALA),
    ("Biona Organic Wholewheat Penne", "Pasta & Noodles", "Live Well", 1.650, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("Biona Organic Wholegrain Spelt Penne", "Pasta & Noodles", "Live Well", 2.100, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("Biona Spelt Fusilli", "Pasta & Noodles", "Live Well", 2.100, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("Biona Organic Asia Noodles", "Pasta & Noodles", "Live Well", 2.630, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("Better Than Noodles", "Pasta & Noodles", "Live Well", 2.070, None, 0.385, "kg", "385 g", LIVE_WELL_HAMALA),
    ("Biona Fusilli Tri Color", "Pasta & Noodles", "Live Well", 1.850, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("BT Pasta Spirals Wholegrain", "Pasta & Noodles", "Live Well", 1.350, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("BT Pasta Penne Wholegrain", "Pasta & Noodles", "Live Well", 1.250, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("Biotropic Basic Muesli", "Breakfast", "Live Well", 2.950, None, 1, "kg", "1 kg", LIVE_WELL_HAMALA),
    ("Turtle Multigrain Flakes Dark Chocolate", "Breakfast", "Live Well", 3.360, None, 0.3, "kg", "300 g", LIVE_WELL_HAMALA),
    ("TC Protein Low Sugar Flakes & Granola", "Breakfast", "Live Well", 3.680, None, 0.3, "kg", "300 g", LIVE_WELL_HAMALA),
    ("TC Oat Crunchy Dark Chocolate", "Breakfast", "Live Well", 3.360, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("TC Cocoa Smiles", "Breakfast", "Live Well", 3.100, None, 0.3, "kg", "300 g", LIVE_WELL_HAMALA),
    ("Biona Sauerkraut", "Canned Goods", "Live Well", 2.050, None, 0.36, "kg", "360 g", LIVE_WELL_HAMALA),
    ("BT Sweet Corn in Jar", "Canned Goods", "Live Well", 1.450, None, 0.35, "kg", "350 g", LIVE_WELL_HAMALA),
    ("Vigo Kombucha Original", "Beverages", "Live Well", 1.650, None, 0.33, "L", "330 ml", LIVE_WELL_HAMALA),
    ("Vigo Kombucha Schisandra", "Beverages", "Live Well", 1.650, None, 0.33, "L", "330 ml", LIVE_WELL_HAMALA),
    ("Vigo Kombucha Acai", "Beverages", "Live Well", 1.650, None, 0.33, "L", "330 ml", LIVE_WELL_HAMALA),
    ("RS GlutenFree Oat Drink", "Milk & Dairy", "Live Well", 1.650, None, 1, "L", "1 L", LIVE_WELL_HAMALA),
    ("Better Than Rice", "Rice", "Live Well", 2.070, None, 0.385, "kg", "385 g", LIVE_WELL_HAMALA),
    ("Biona Organic Mayonnaise with Sunflower Oil", "Spices & Condiments", "Live Well", 2.840, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("Biona Organic Dijon Mustard", "Spices & Condiments", "Live Well", 2.420, None, 0.2, "kg", "200 g", LIVE_WELL_HAMALA),
    ("Biotropic Passata Tomatoes", "Canned Goods", "Live Well", 1.930, None, 0.6, "L", "600 ml", LIVE_WELL_HAMALA),
    ("Biona Himalayan Salt Fine", "Spices & Condiments", "Live Well", 3.360, None, 0.5, "kg", "500 g", LIVE_WELL_HAMALA),
    ("Sonnentor Bay Leaves", "Spices & Condiments", "Live Well", 1.680, None, 0.01, "kg", "10 g", LIVE_WELL_HAMALA),
    ("Biotropic Sunflower Seed Oil for Roasting", "Cooking Oil", "Live Well", 4.150, None, 0.75, "L", "750 ml", LIVE_WELL_HAMALA),
    ("Iliada Olive Oil", "Cooking Oil", "Live Well", 7.110, None, 0.75, "L", "750 ml", LIVE_WELL_HAMALA),
    ("Biona Apple Cider Vinegar", "Spices & Condiments", "Live Well", 2.730, None, 0.5, "L", "500 ml", LIVE_WELL_HAMALA),
    ("Biona Organic Coconut Palm Sugar", "Sugar", "Live Well", 2.500, None, 0.25, "kg", "250 g", LIVE_WELL_HAMALA),
    ("BT Sesame Seed Oil", "Cooking Oil", "Live Well", 4.600, None, 0.5, "L", "500 ml", LIVE_WELL_HAMALA),
    ("Smart Organic Dragon Chickpea Flour", "Flour & Baking", "Live Well", 1.500, None, 0.2, "kg", "200 g", LIVE_WELL_HAMALA),
    ("Smart Organic Dragon Tapioca Flour", "Flour & Baking", "Live Well", 1.550, None, 0.2, "kg", "200 g", LIVE_WELL_HAMALA),


    ("Coconut Hard", "Fruits & Vegetables", "Al Markazi Central Market", 0.532, None, 1, "pcs", "1 piece", AL_MARKAZI_HAMALA),
    ("Red Onion Bag", "Fruits & Vegetables", "Al Markazi Central Market", 1.640, None, 2.5, "kg", "2.5 kg", AL_MARKAZI_HAMALA),
    ("Okra", "Fruits & Vegetables", "Al Markazi Central Market", 0.890, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Red Onion India", "Fruits & Vegetables", "Al Markazi Central Market", 0.325, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Green Chilli India", "Fruits & Vegetables", "Al Markazi Central Market", 0.790, None, 0.25, "kg", "250 g", AL_MARKAZI_HAMALA),
    ("Lebanon Potato", "Fruits & Vegetables", "Al Markazi Central Market", 0.370, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Red Cabbage", "Fruits & Vegetables", "Al Markazi Central Market", 0.575, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Sweet Potato", "Fruits & Vegetables", "Al Markazi Central Market", 0.650, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Garlic", "Fruits & Vegetables", "Al Markazi Central Market", 0.900, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Green Seedless Lime", "Fruits & Vegetables", "Al Markazi Central Market", 0.850, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("White Peeled Onion", "Fruits & Vegetables", "Al Markazi Central Market", 0.450, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Potato", "Fruits & Vegetables", "Al Markazi Central Market", 0.385, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Red Onion Yamman", "Fruits & Vegetables", "Al Markazi Central Market", 0.340, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Ginger", "Fruits & Vegetables", "Al Markazi Central Market", 1.700, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Lemon Packet", "Fruits & Vegetables", "Al Markazi Central Market", 0.700, None, 1, "pack", "1 pack", AL_MARKAZI_HAMALA),
    ("Turkey Lemon", "Fruits & Vegetables", "Al Markazi Central Market", 0.525, None, 0.5, "kg", "Approx. 500 g", AL_MARKAZI_HAMALA),
    ("Red Peeled Onion", "Fruits & Vegetables", "Al Markazi Central Market", 0.550, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Fry Chilli", "Fruits & Vegetables", "Al Markazi Central Market", 0.475, None, 0.25, "kg", "250 g", AL_MARKAZI_HAMALA),
    ("White Onion", "Fruits & Vegetables", "Al Markazi Central Market", 0.440, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("White Onion Spain", "Fruits & Vegetables", "Al Markazi Central Market", 0.850, None, 0.5, "kg", "500 g", AL_MARKAZI_HAMALA),
    ("Red Cherry Tomato Plums", "Fruits & Vegetables", "Al Markazi Central Market", 1.100, None, 1, "pack", "1 pack", AL_MARKAZI_HAMALA),
    ("Peeled Garlic", "Fruits & Vegetables", "Al Markazi Central Market", 0.580, None, 0.25, "kg", "250 g", AL_MARKAZI_HAMALA),

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
    ("LuLu Butter Jeera Biscuits", "Snacks", "LuLu", 0.790, 0.990, 0.72, "kg", "8 x 90 g", LULU_EXCLUSIVE),
]

def demo_products():
    """Return source-backed retailer snapshot rows for the app's catalogue."""
    products = [{
        "product_name": name,
        "category": category,
        "store": store,
        "city": "Hamala" if store in {"Nass Foods", "Live Well", "Al Markazi Central Market"} else "All Bahrain",
        "price": price,
        "original_price": original,
        "quantity": quantity,
        "unit": unit,
        "pack_description": pack,
        "source_url": url,
        "collected_at": CHECKED,
        "checked_at": CHECKED,
        "data_status": "Talabat listing" if store in {"Nass Foods", "Live Well", "Al Markazi Central Market"} else "Website listing",
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
