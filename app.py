import streamlit as st
import pandas as pd
import plotly.express as px

from core.database import (
    initialize_database,
    save_observation,
    get_history
)

from core.comparator import compare_products

from scrapers.demo import demo_products


# ==========================================
# Setup
# ==========================================

st.set_page_config(
    page_title="PriceScout OSINT",
    page_icon="🛒",
    layout="wide"
)

initialize_database()


# ==========================================
# Styling
# ==========================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    color: #777;
    font-size: 18px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

.price {
    font-size: 28px;
    font-weight: 700;
}

.offer {
    color: #0a8f3d;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# Header
# ==========================================

st.markdown(
    '<div class="main-title">🛒 PriceScout</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Bahrain Retail OSINT & Price Comparison'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# ==========================================
# Data
# ==========================================

products = demo_products()


# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("🔎 Search")

categories = [
    "All",
    "Chicken",
    "Water",
    "Milk",
    "Rice",
    "Eggs",
    "Cleaning"
]

category = st.sidebar.selectbox(
    "Category",
    categories
)

search = st.sidebar.text_input(
    "Search",
    placeholder="chicken, water..."
)

criterion = st.sidebar.selectbox(
    "Compare by",
    [
        "Unit price",
        "Total price",
        "Discount"
    ]
)


# ==========================================
# Filter
# ==========================================

filtered = products.copy()

if category != "All":

    filtered = [
        p for p in filtered
        if p["category"] == category
    ]


if search:

    query = search.lower()

    filtered = [
        p for p in filtered
        if query in p["product_name"].lower()
    ]


criterion_map = {
    "Unit price": "unit_price",
    "Total price": "total_price",
    "Discount": "discount"
}

results = compare_products(
    filtered,
    criterion_map[criterion]
)


# ==========================================
# Tabs
# ==========================================

compare_tab, offers_tab, history_tab = st.tabs(
    [
        "🔎 Compare",
        "🔥 Latest Offers",
        "📊 Price History"
    ]
)


# ==========================================
# Compare
# ==========================================

with compare_tab:

    st.header("Current Prices")

    if not results:

        st.info(
            "No products found."
        )

    else:

        for product in results:

            discount = product.get(
                "discount"
            )

            unit_price = product.get(
                "unit_price"
            )

            col1, col2, col3 = st.columns(
                [4, 2, 2]
            )

            with col1:

                st.subheader(
                    product["product_name"]
                )

                st.write(
                    f'🏪 {product["store"]}'
                )

                st.write(
                    f'📦 {product["pack_description"]}'
                )

            with col2:

                st.markdown(
                    f"""
                    <div class="price">
                    {product["price"]:.3f} BHD
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if unit_price:

                    st.write(
                        f"{unit_price:.3f} BHD/"
                        f"{product['unit']}"
                    )

            with col3:

                if discount:

                    st.markdown(
                        f"""
                        <div class="offer">
                        🔥 {discount}% OFF
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.write(
                        "No advertised discount"
                    )

            source = product.get(
                "source_url"
            )

            if source:

                st.caption(
                    f"Source: {source}"
                )

            st.divider()


# ==========================================
# Latest Offers
# ==========================================

with offers_tab:

    st.header("🔥 Latest Offers")

    offers = [
        p for p in results
        if p.get("discount")
        and p["discount"] > 0
    ]

    if not offers:

        st.info(
            "No current offers found."
        )

    else:

        offers.sort(
            key=lambda x: x["discount"],
            reverse=True
        )

        for offer in offers:

            st.success(
                f'🔥 {offer["product_name"]} — '
                f'{offer["discount"]}% OFF at '
                f'{offer["store"]} '
                f'({offer["price"]:.3f} BHD)'
            )

            if offer.get("source_url"):

                st.markdown(
                    f'[View source]({offer["source_url"]})'
                )


# ==========================================
# History
# ==========================================

with history_tab:

    st.header("📊 Price History")

    if results:

        selected = st.selectbox(
            "Product",
            [
                p["product_name"]
                for p in results
            ]
        )

        history = get_history(
            selected
        )

        if history:

            df = pd.DataFrame(
                history,
                columns=[
                    "Product",
                    "Store",
                    "Price",
                    "Collected"
                ]
            )

            df["Collected"] = pd.to_datetime(
                df["Collected"]
            )

            fig = px.line(
                df,
                x="Collected",
                y="Price",
                color="Store",
                markers=True,
                title=selected
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info(
                "No historical observations yet."
            )


# ==========================================
# OSINT explanation
# ==========================================

with st.expander(
    "ℹ️ How this OSINT tool works"
):

    st.markdown("""
    **PriceScout uses publicly accessible or authorized
    retail information.**

    The tool:

    1. Collects product information from permitted sources.
    2. Records the source URL and collection time.
    3. Extracts prices, package sizes and advertised discounts.
    4. Normalizes quantities such as kg and litres.
    5. Compares products across stores.
    6. Stores observations so price changes can be analyzed.

    The project does not attempt to access private accounts,
    bypass authentication, or obtain confidential information.
    """)
