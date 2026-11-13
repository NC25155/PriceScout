import os
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

# On Windows, the default database is stored in the project folder.
# On Streamlit Community Cloud, set DATABASE_PATH to a persistent mounted
# database location or use an external database before expecting durability
# across container replacement/redeployments.
DATABASE_PATH = Path(os.getenv("DATABASE_PATH", "data/pricescout.db"))


def connect():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH, timeout=20)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS observations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                category TEXT,
                store TEXT NOT NULL,
                price REAL NOT NULL,
                original_price REAL,
                quantity REAL,
                unit TEXT,
                pack_description TEXT,
                source_url TEXT,
                collected_at TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_observations_product_date
            ON observations(product_name, collected_at)
        """)


def record_observations(products):
    """Save at most one observation per product/store per calendar day."""
    saved = 0
    with connect() as conn:
        for product in products:
            price = product.get("price")
            name = product.get("product_name")
            store = product.get("store")
            if price is None or not name or not store:
                continue

            now = product.get("collected_at") or datetime.now(timezone.utc).isoformat(timespec="seconds")
            day = now[:10]
            exists = conn.execute("""
                SELECT 1 FROM observations
                WHERE product_name = ? AND store = ? AND substr(collected_at, 1, 10) = ?
                LIMIT 1
            """, (name, store, day)).fetchone()
            if exists:
                continue

            conn.execute("""
                INSERT INTO observations (
                    product_name, category, store, price, original_price,
                    quantity, unit, pack_description, source_url, collected_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name, product.get("category"), store, float(price),
                product.get("original_price"), product.get("quantity"),
                product.get("unit"), product.get("pack_description"),
                product.get("source_url"), now
            ))
            saved += 1
    return saved


def get_history(product_name=None):
    with connect() as conn:
        if product_name:
            return conn.execute("""
                SELECT product_name, store, price, collected_at
                FROM observations
                WHERE product_name = ?
                ORDER BY collected_at
            """, (product_name,)).fetchall()
        return conn.execute("""
            SELECT product_name, store, price, collected_at
            FROM observations
            ORDER BY collected_at
        """).fetchall()


def get_history_products():
    with connect() as conn:
        rows = conn.execute("""
            SELECT DISTINCT product_name
            FROM observations
            ORDER BY product_name COLLATE NOCASE
        """).fetchall()
    return [row[0] for row in rows]
