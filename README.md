# 🛒 PriceScout

**Bahrain grocery price research and comparison**

[![Open PriceScout](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pricescout-wx3xtlw5pd82ijvlixf95w.streamlit.app/)

🌐 **Live website:** https://pricescout-wx3xtlw5pd82ijvlixf95w.streamlit.app/  
💻 **GitHub:** https://github.com/NC25155/PriceScout

PriceScout is a Python + Streamlit project for exploring grocery listings, comparing pack sizes and unit prices, and recording dated observations from successfully collected public catalogue data.

## Features

- Search and category filters
- Bahrain retailer links and area filters
- Unit-price normalization (kg / litre where package information is available)
- Discount calculations when an original price is supplied by the source
- Chicken product watchlist, including Americana chicken breast (2 kg), chicken breast fillets, chicken strips, chicken nuggets and tempura nuggets
- Price-history charts backed by a repository-stored CSV updated by GitHub Actions
- Clear separation between live-collected data and illustrative sample data
- Windows Command Prompt and Linux setup instructions

## Data and history

The app attempts to collect public LuLu catalogue information and caches a successful fetch for up to six hours. A separate GitHub Actions job appends a dated observation at most once per product/store/day to a CSV file committed to the repository.

**Important:** The current public collector only covers the catalogue page configured in `scrapers/lulu.py`. Other retailer links are navigation links, not verified automated feeds. When the collector cannot confirm current prices, the app switches to clearly labelled illustrative sample data. Sample values are not live offers.

The history CSV is committed to GitHub, so it is not dependent on Streamlit's temporary container filesystem. Each successful daily collector run creates a Git commit containing the new observations.

## Install on Windows (CMD)

1. Install Python 3.11 or newer from https://www.python.org/downloads/ . During installation, enable **Add Python to PATH**.
2. Download the repository using GitHub's **Code → Download ZIP**, then extract it.
3. Open the extracted `PriceScout` folder in File Explorer.
4. Click the address bar, type `cmd`, and press Enter.
5. Run:

```cmd
py -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

6. Open the local address printed in CMD (usually http://localhost:8501).

To start it again later:

```cmd
cd path\to\PriceScout
.venv\Scripts\activate
py -m streamlit run app.py
```

## Install on Kali Linux / Debian-based Linux

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Project structure

```text
PriceScout/
├── app.py
├── core/
│   ├── comparator.py
│   ├── database.py
│   └── normalizer.py
├── scrapers/
│   ├── demo.py
│   └── lulu.py
├── data/
├── tests/
├── requirements.txt
└── README.md
```

## Run tests

```cmd
py -m pip install pytest
py -m pytest
```

## Responsible collection

PriceScout is intended for public or authorized retail catalogue information. It does not attempt to bypass logins, access controls, or private accounts. Retailer pages may change their structure or terms; collection should be used only where permitted.

## Project links

- **Live app:** https://pricescout-wx3xtlw5pd82ijvlixf95w.streamlit.app/
- **Repository:** https://github.com/NC25155/PriceScout


## Automatic daily price history

GitHub Actions is configured to run the public LuLu catalogue collector every day at **06:15 Bahrain time** (03:15 UTC). You can also start it manually from **Actions → Daily Price History → Run workflow**.

Successful observations are appended to `data/pricescout_history.csv`, committed to the repository, and displayed in the app's History tab. This repository-backed CSV survives Streamlit container restarts. The collector saves at most one observation per product/store/day and fails without writing fake history if it cannot parse any products.

The history begins with the first successful run; it cannot reconstruct earlier prices. Only the LuLu public catalogue currently has an automated collector. Other retailer links are not automatic feeds.

If the workflow does not run, check that GitHub Actions are enabled and repository workflow permissions allow read/write access.
