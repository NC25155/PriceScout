from datetime import datetime, timezone
import pandas as pd
import plotly.express as px
import streamlit as st

from core.comparator import compare_products
from scrapers.demo import demo_products
from scrapers.lulu import collect_lulu

APP_URL = "https://pricescout-wx3xtlw5pd82ijvlixf95w.streamlit.app/"
GITHUB_URL = "https://github.com/NC25155/PriceScout"

st.set_page_config(
    page_title="PriceScout | Bahrain Grocery Prices",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
:root {
  color-scheme: light dark;
  --ps-bg:#f7f9fc; --ps-panel:#ffffff; --ps-ink:#172033;
  --ps-muted:#687386; --ps-line:#e5eaf2; --ps-soft:#eef5ff;
}
[data-theme="dark"], [data-testid="stAppViewContainer"][data-theme="dark"] {
  --ps-bg:#0e1117; --ps-panel:#171b24; --ps-ink:#f1f5fb;
  --ps-muted:#a6b0c0; --ps-line:#303846; --ps-soft:#202b3b;
}
@media (prefers-color-scheme: dark) {
  html:not([data-theme="light"]) {
    --ps-bg:#0e1117; --ps-panel:#171b24; --ps-ink:#f1f5fb;
    --ps-muted:#a6b0c0; --ps-line:#303846; --ps-soft:#202b3b;
  }
}
.block-container {max-width:1380px; padding-top:2rem; padding-bottom:3rem;}
[data-testid="stAppViewContainer"] {background:var(--ps-bg); color:var(--ps-ink);}
[data-testid="stHeader"] {background:transparent;}
[data-testid="stSidebar"] {background:var(--ps-panel); border-right:1px solid var(--ps-line);}
.ps-hero {padding:1.45rem 1.6rem; border:1px solid var(--ps-line); border-radius:20px;
background:linear-gradient(120deg,var(--ps-panel) 0%,var(--ps-soft) 100%); margin-bottom:1rem;}
.ps-kicker {font-size:.78rem; letter-spacing:.12em; text-transform:uppercase;
color:var(--ps-muted); font-weight:700;}
.ps-title {font-size:2.35rem; line-height:1.15; font-weight:800; color:var(--ps-ink); margin:.25rem 0;}
.ps-sub {color:var(--ps-muted); font-size:1rem;}
.ps-card {background:var(--ps-panel); border:1px solid var(--ps-line); border-radius:16px;
padding:1rem 1.1rem; min-height:105px;}
.ps-label {color:var(--ps-muted); font-size:.82rem; font-weight:600;}
.ps-value {color:var(--ps-ink); font-size:1.7rem; font-weight:800; margin-top:.2rem;}
.ps-note {color:var(--ps-muted); font-size:.78rem;}
div[data-testid="stMetric"] {background:var(--ps-panel); border:1px solid var(--ps-line);
padding:14px 16px; border-radius:15px;}
div[data-testid="stMetric"] label, div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricDelta"] {color:var(--ps-ink);}
.stTabs [data-baseweb="tab-list"] {gap:8px;}
.stTabs [data-baseweb="tab"] {border-radius:10px; padding:10px 16px;
background:var(--ps-panel); color:var(--ps-ink);}
.stTabs [aria-selected="true"] {border-bottom-color:#4f8cff !important;}
[data-testid="stDataFrame"], [data-testid="stTable"] {border:1px solid var(--ps-line); border-radius:12px;}
input, textarea {color:var(--ps-ink);}
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
        "Price checked": p.get("checked_at") or str(p.get("collected_at") or "")[:10],
        "Data source": p.get("data_status", "Source listing"),
        "Retailer link": p.get("source_url", ""),
    } for p in rows])
    st.dataframe(
        frame,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Price (BHD)": st.column_config.NumberColumn("Price (BHD)", format="%.3f"),
            "Retailer link": st.column_config.LinkColumn("Retailer link", display_text="Open listing"),
        },
    )


with st.sidebar:
    st.markdown("## 🛒 PriceScout")
    st.caption("Bahrain grocery price research")
    st.divider()
    st.markdown("**Find products**")
    search = st.text_input("Search by name", placeholder="e.g. Americana, chicken strips")
    categories = [
        "All", "Rice", "Flour & Baking", "Sugar", "Cooking Oil",
        "Chicken", "Meat & Seafood", "Eggs", "Milk & Dairy", "Water",
        "Laundry", "Paper & Tissue", "Cleaning", "Personal Care",
        "Breakfast", "Canned Goods", "Pasta & Noodles", "Frozen Food",
        "Bakery", "Fruits & Vegetables", "Snacks", "Beverages",
        "Coffee & Tea", "Spices & Condiments", "Dates & Dried Fruit",
    ]
    category = st.selectbox("Category", categories)
    area = st.selectbox("Area", ["All", "Juffair", "Riffa", "Hamala", "Arad"])
    sort_by = st.selectbox("Sort results by", ["Unit price", "Total price", "Discount"])
    st.divider()
    refresh = st.button("↻ Refresh public prices", use_container_width=True)
    st.caption("Public catalogue refresh is cached for up to 6 hours. Historical prices are collected automatically each day by GitHub Actions.")
    st.markdown(f"[Open live website]({APP_URL})")
    st.markdown(f"[View source code]({GITHUB_URL})")

if refresh:
    load_live_catalog.clear()

with st.spinner("Checking the public catalogue…"):
    live_products, live_error = load_live_catalog()

# Use source-backed catalogue snapshots even when the live scraper is
# unavailable. Add live LuLu rows when the scraper can validate them.
snapshot_products = demo_products()
products = snapshot_products + live_products
live_mode = bool(live_products)

st.markdown(f"""
<div class="ps-hero">
  <div class="ps-kicker">Bahrain • Grocery intelligence</div>
  <div class="ps-title">PriceScout</div>
  <div class="ps-sub">Search for a grocery item to compare prices, or browse offers and price history.</div>
</div>
""", unsafe_allow_html=True)

st.caption(
    f"{len(snapshot_products)} source-backed retailer listings checked 13 Nov 2026"
    + (f" · plus {len(live_products)} validated live LuLu listings" if live_mode else "")
    + " · Open each retailer link to confirm current price and stock."
)
if live_error:
    st.caption(f"Live LuLu refresh unavailable; showing the dated retailer snapshots instead: {live_error}")

last_checked = datetime.now().astimezone().strftime("%d %b %Y, %H:%M %Z")
st.caption(f"Page checked: {last_checked} · Live catalogue cache: up to 6 hours · Retailer snapshot prices are dated and may change.")

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

# Keep the comparison area hidden until the user searches for a product.
if search.strip():
    st.subheader(f"🔎 Price comparison for “{search.strip()}”")
    st.caption("Prices are dated retailer listing snapshots unless marked as live. Check the retailer page before purchase.")
    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("Products in view", len(results))
    col_b.metric("Stores represented", len({p.get("store") for p in results}))
    discount_count = sum(1 for p in results if (p.get("discount") or 0) > 0)
    col_c.metric("Advertised discounts", discount_count)
    col_d.metric("Data mode", "Live" if live_mode else "Sample")
    product_table(results)
    if results:
        st.caption("Compare like-for-like pack sizes and varieties. A lower price per kg is not necessarily the same rice variety or quality.")

offers_tab, history_tab, about_tab = st.tabs([
    "🏷️ Offers", "📈 Price history", "ℹ️ About"
])

with offers_tab:
    st.subheader("Discounts")
    # Calculate discounts before filtering: raw scraper rows do not yet contain
    # the derived "discount" field.
    offer_candidates = compare_products(filtered, "discount")
    offers = [p for p in offer_candidates if (p.get("discount") or 0) > 0]
    if not offers:
        st.info("No verified discounted products are available in this view.")
    else:
        st.caption("Discounts appear only when the retailer listing provides both a current price and an original price.")
        product_table(offers)

with history_tab:
    st.subheader("Automatic price history")
    history_file = "data/pricescout_history.csv"
    try:
        history_df = pd.read_csv(history_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        history_df = pd.DataFrame(columns=["product_name", "store", "price", "collected_at", "source_url"])

    if history_df.empty:
        st.info("The scheduled collector has not saved its first successful observation yet. GitHub Actions runs daily; history appears here after a successful collection.")
    else:
        history_df["collected_at"] = pd.to_datetime(history_df["collected_at"], errors="coerce", utc=True)
        history_products = sorted(history_df["product_name"].dropna().unique().tolist())
        selected = st.selectbox("Choose a product", history_products)
        view = history_df[history_df["product_name"] == selected].copy()
        fig = px.line(view, x="collected_at", y="price", color="store", markers=True,
                      title=f"{selected} — observed prices (BHD)")
        fig.update_layout(template="plotly_white", yaxis_title="Price (BHD)", xaxis_title="Observation date")
        st.plotly_chart(fig, use_container_width=True)
        display = view.rename(columns={
            "product_name": "Product", "store": "Store", "price": "Price (BHD)",
            "collected_at": "Collected (UTC)", "source_url": "Source"
        })
        st.dataframe(display.sort_values("Collected (UTC)", ascending=False), use_container_width=True, hide_index=True)
        st.caption(f"{len(view)} saved observations · History is maintained by a daily GitHub Actions run.")
    st.caption("Only successfully collected public catalogue prices are recorded. A failed collection does not create a history point.")

with about_tab:
    st.subheader("About PriceScout")
    st.write("PriceScout is a Bahrain-focused grocery price research project. It normalizes pack sizes where possible, compares unit prices, and keeps a dated record of successfully collected public prices.")
    st.markdown("**Data integrity**")
    st.write("- Live data is separated from illustrative sample data.")
    st.write("- A product is not labelled as in stock unless a source confirms it.")
    st.write("- The collector does not bypass logins or access controls.")
    st.write("- Price history is appended by a scheduled daily GitHub Actions collector and stored in the repository.")
    st.markdown(f"**Project links:** [Live app]({APP_URL}) · [GitHub repository]({GITHUB_URL})")
    st.caption("Updated interface · Bahrain retail catalogue · Python + Streamlit")
