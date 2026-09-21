# 🛒 PriceScout OSINT

PriceScout is a Bahrain-focused OSINT retail price comparison tool.

## Purpose

The application collects publicly accessible or authorized retail information and organizes it into a searchable price comparison system.

Users can explore categories such as:

- Chicken
- Water
- Milk
- Rice
- Eggs
- Cleaning products

## Features

- Product search
- Category filtering
- Store comparison
- Price comparison
- Price-per-kg comparison
- Price-per-litre comparison
- Advertised discount detection
- Latest offers
- Price history
- Source URLs
- Collection timestamps

## OSINT Methodology

PriceScout follows:

Public source
→ Collection
→ Extraction
→ Normalization
→ Correlation
→ Analysis
→ Presentation

The tool only uses publicly accessible or authorized information.

It does not:

- Access private accounts
- Bypass authentication
- Collect passwords
- Circumvent security controls
- Attempt to access confidential information

## Technology

Python

Streamlit

SQLite

Pandas

BeautifulSoup

Requests

Plotly

## Run

Install dependencies:

    pip install -r requirements.txt

Run:

    streamlit run app.py

## Project structure

    PriceScout/
    ├── app.py
    ├── core/
    ├── scrapers/
    ├── data/
    ├── tests/
    ├── requirements.txt
    └── README.md

## Disclaimer

Retail websites may change their page structure or access policies.
Collectors must only be used against sources where automated
collection is permitted.
