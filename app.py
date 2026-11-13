from datetime import datetime, timezone
import pandas as pd
import plotly.express as px
import streamlit as st

from core.comparator import compare_products
from core.database import initialize_database, record_observations, get_history, get_history_products
from scrapers.demo import demo_products, CHICKEN_WATCHLIST
from scrapers.lulu import collect_lulu

APP_URL = "https://pricescout-wx3xtlw5pd82ijvlixf95w.streamlit.app/"
GITHUB_URL = "https://github.com/NC25155/PriceScout"

st.set_page_config(
    page_title="PriceScout | Bahrain Grocery Prices",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_database()

st.markdown("""
<style>
:root { --ps-ink:#172033; --ps-muted:#687386; --ps-line:#e8edf3; }
.block-container {max-width: 1380px; padding-top: 2rem; padding-bottom: 3rem;}
[data-testid="stAppViewContainer"] {background: #f7f9fc;}
[data-testid="stSidebar"] {background: #fff; border-right: 1px solid #e8edf3;}
.ps-hero {padding: 1.45rem 1.6rem; border:1px solid #e5eaf2; border-radius:20px;
background:linear-gradient(120deg,#ffffff 0%,#eef5ff 100%); margin-bottom:1rem;}
.ps-kicker {font-size:.78rem; letter-spacing:.12em; text-transform:uppercase;
color:#536b8a; font-weight:700;}
.ps-title {font-size:2.35rem; line-height:1.15; font-weight:800; color:#172033; margin:.25rem 0;}
.ps-sub {color:#65738a; font-size:1rem;}
.ps-card {background:#fff; border:1px solid #e7ecf3; border-radius:16px;
padding:1rem 1.1rem; min-height:105px;}
.ps-label {color:#69778c; font-size:.82rem; font-weight:600;}
.ps-value {color:#172033; font-size:1.7rem; font-weight:800; margin-top:.2rem;}
.ps-note {color:#758197; font-size:.78rem;}
div[data-testid="stMetric"] {background:#fff; border:1px solid #e7ecf3;
padding:14px 16px; border-radius:15px;}
.stTabs [data-baseweb="tab-list"] {gap:8px;}
.stTabs [data-baseweb="tab"] {border-radius:10px; padding:10px 16px; background:#fff;}
a {text-decoration:none;}
</style>
""", unsafe_allow_html=True)


@st.cache_data(ttl=6 * 60 * 60, show_spinner=False)
def load_live_catalog():
    """Fetch permitted public LuLu catalogue data; cache for six hours."""
    try:
        rows = collect_lulu()
        cleaned = []
        for row in rows:
            if row.get("product_name") and row.get("price") is not None:
                row["city"] = "All Bahrain"
                row["data_status"] = "Live source"
                cleaned.append(row)
        return cleaned, None
    except Exception as exc:
        return [], str(exc)


def money(value):
    return "—" if value is None else f"{value:.3f} BHD"


def product_table(rows):
    if not rows:
        st.info("No matching products in this view.")
        return
    frame = pd.DataFrame([{
        "Product": p.get("product_name", ""),
        "Store": p.get("store", ""),
        "Area": p.get("city", "Not specified"),
        "Pack": p.get("pack_description") or "Pack not identified",
        "Price (BHD)": p.get("price"),
        "Unit price": (
            f'{p["unit_price"]:.3f} BHD/{p["unit"]}'
            if p.get("unit_price") is not None and p.get("unit")
            else "Not available"
        ),
        "Discount": (
            f'{p["discount"]:.1f}%'
            if p.get("discount") is not None and p.get("discount") > 0
            else "—"
        ),
    } for p in rows])
    st.dataframe(frame, use_container_width=True, hide_index=True)


with st.sidebar:
    st.markdown("## 🛒 PriceScout")
    st.caption("Bahrain grocery price research")
    st.divider()
    st.markdown("**Find products**")
    search = st.text_input("Search by name", placeholder="e.g. Americana, chicken strips")
    categories = [
        "All", "Chicken", "Meat & Seafood", "Water", "Milk", "Dairy & Cheese",
        "Rice", "Eggs", "Cleaning", "Bakery", "Cooking Oil",
        "Fruits & Vegetables", "Dates & Dried Fruit", "Snacks",
        "Frozen Food", "Beverages", "Coffee & Tea", "Canned Goods",
        "Pasta & Noodles", "Spices & Condiments", "Personal Care",
    ]
    category = st.selectbox("Category", categories)
    area = st.selectbox("Area", ["All", "Juffair", "Riffa", "Hamala", "Arad"])
    sort_by = st.selectbox("Sort results by", ["Unit price", "Total price", "Discount"])
    st.divider()
    refresh = st.button("↻ Refresh public prices", use_container_width=True)
    st.caption("Public catalogue refresh is cached for up to 6 hours.")
    st.markdown(f"[Open live website]({APP_URL})")
    st.markdown(f"[View source code]({GITHUB_URL})")

if refresh:
    load_live_catalog.clear()

with st.spinner("Checking the public catalogue…"):
    live_products, live_error = load_live_catalog()

if live_products:
    products = live_products
    live_mode = True
    # Daily de-duplication means repeated page visits do not create fake history points.
    saved_count = record_observations(products)
else:
    products = demo_products()
    live_mode = False
    saved_count = 0

st.markdown(f"""
<div class="ps-hero">
  <div class="ps-kicker">Bahrain • Grocery intelligence</div>
  <div class="ps-title">PriceScout</div>
  <div class="ps-sub">Compare grocery prices, review product packs, and follow verified price changes.</div>
</div>
""", unsafe_allow_html=True)

if live_mode:
    st.success(f"Live public catalogue data loaded from LuLu. {len(products)} products found. New daily history points saved: {saved_count}.")
else:
    st.warning("Preview mode: live catalogue data could not be confirmed. The comparison below uses illustrative sample data, not verified current store prices.")
    if live_error:
        st.caption(f"Collector note: {live_error}")
    else:
        st.caption("The public catalogue did not return parseable product records. Try refreshing later.")

last_checked = datetime.now().astimezone().strftime("%d %b %Y, %H:%M %Z")
st.caption(f"Page checked: {last_checked} · Catalogue cache: up to 6 hours · Sample values are clearly marked.")

filtered = products[:]
if category != "All":
    filtered = [p for p in filtered if p.get("category") == category]
if area != "All":
    filtered = [p for p in filtered if p.get("city") in (area, "All Bahrain")]
if search.strip():
    q = search.casefold()
    filtered = [p for p in filtered if q in p.get("product_name", "").casefold()]

criterion = {"Unit price": "unit_price", "Total price": "total_price", "Discount": "discount"}[sort_by]
results = compare_products(filtered, criterion) if filtered else []

if not live_mode:
    st.info("Sample prices are for interface testing only. They are not live offers and should not be used as current shopping prices.", icon="ℹ️")

col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("Products in view", len(results))
col_b.metric("Stores represented", len({p.get("store") for p in results}))
discount_count = sum(1 for p in results if (p.get("discount") or 0) > 0)
col_c.metric("Advertised discounts", discount_count)
col_d.metric("Data mode", "Live" if live_mode else "Sample")

compare_tab, chicken_tab, offers_tab, history_tab, about_tab = st.tabs([
    "🔎 Price comparison", "🍗 Chicken finder", "🏷️ Offers", "📈 Price history", "ℹ️ About"
])

with compare_tab:
    st.subheader("Product comparison")
    product_table(results)
    if results and live_mode:
        st.caption("Prices are taken from the public source shown by the collector. Confirm the pack and availability on the retailer site before relying on a listing.")
    elif results:
        st.caption("The rows shown are sample data. Source links open retailer storefronts, but do not verify the displayed sample price.")

with chicken_tab:
    st.subheader("Chicken products to look for")
    st.write("The following product types are included in the catalogue watchlist. Availability and prices are not claimed unless a retailer listing is actually collected.")
    for item in CHICKEN_WATCHLIST:
        with st.container(border=True):
            left, right = st.columns([4, 1])
            with left:
                st.markdown(f"**{item['name']}**")
                st.caption(item["search_terms"])
            with right:
                st.caption("Watchlist")
    st.divider()
    st.markdown("**Retailer links**")
    st.caption("These links open the retailer storefronts. They do not confirm that a specific chicken product is stocked.")
    retailer_links = [
        ("LuLu", "https://gcc.luluhypermarket.com/en-bh/"),
        ("Alosra", "https://www.talabat.com/bahrain/grocery/50392/alosra-aljuffair"),
        ("HyperMax", "https://www.talabat.com/bahrain/grocery/711604/hypermax-riffa-alshamali-north-riffa"),
        ("Al Jazira", "https://www.talabat.com/bahrain/grocery/727495/al-jazira-supermarket-hamala"),
        ("Talal Markets", "https://www.talabat.com/bahrain/grocery/718139/talal-markets-arad-new"),
    ]
    link_cols = st.columns(len(retailer_links))
    for col, (name, url) in zip(link_cols, retailer_links):
        col.markdown(f"[{name}]({url})")

with offers_tab:
    st.subheader("Discounts")
    offers = [p for p in results if (p.get("discount") or 0) > 0]
    if not offers:
        st.info("No verified discounted products are available in this view.")
    elif not live_mode:
        st.warning("These are illustrative sample discounts, not verified current offers.")
        product_table(offers)
    else:
        product_table(offers)

with history_tab:
    st.subheader("Observed price history")
    history_products = get_history_products()
    if not history_products:
        st.info("No verified price observations have been saved yet. History starts when the public collector successfully retrieves a product price.")
    else:
        selected = st.selectbox("Choose a product", history_products)
        history = get_history(selected)
        if history:
            df = pd.DataFrame(history, columns=["Product", "Store", "Price", "Collected"])
            df["Collected"] = pd.to_datetime(df["Collected"], errors="coerce")
            fig = px.line(df, x="Collected", y="Price", color="Store", markers=True,
                          title=f"{selected} — observed prices (BHD)")
            fig.update_layout(template="plotly_white", yaxis_title="Price (BHD)", xaxis_title="Observation date")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df.sort_values("Collected", ascending=False), use_container_width=True, hide_index=True)
        st.caption("History records are observations, not predictions. A new point is saved at most once per product/store/day.")

with about_tab:
    st.subheader("About PriceScout")
    st.write("PriceScout is a Bahrain-focused grocery price research project. It normalizes pack sizes where possible, compares unit prices, and keeps a dated record of successfully collected public prices.")
    st.markdown("**Data integrity**")
    st.write("- Live data is separated from illustrative sample data.")
    st.write("- A product is not labelled as in stock unless a source confirms it.")
    st.write("- The collector does not bypass logins or access controls.")
    st.write("- Price history is created from collected observations, not from page refreshes.")
    st.markdown(f"**Project links:** [Live app]({APP_URL}) · [GitHub repository]({GITHUB_URL})")
    st.caption("Updated interface · Bahrain retail catalogue · Python + Streamlit + SQLite")
