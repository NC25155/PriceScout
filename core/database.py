import sqlite3
from pathlib import Path
from datetime import datetime


DATABASE_PATH = Path("data/pricescout.db")


def connect():
    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    return sqlite3.connect(DATABASE_PATH)


def initialize_database():

    conn = connect()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
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

    conn.commit()
    conn.close()


def save_observation(product):

    conn = connect()

    conn.execute("""
        INSERT INTO observations (
            product_name,
            category,
            store,
            price,
            original_price,
            quantity,
            unit,
            pack_description,
            source_url,
            collected_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product["product_name"],
        product["category"],
        product["store"],
        product["price"],
        product.get("original_price"),
        product.get("quantity"),
        product.get("unit"),
        product.get("pack_description"),
        product.get("source_url"),
        product.get(
            "collected_at",
            datetime.now().isoformat(timespec="seconds")
        )
    ))

    conn.commit()
    conn.close()


def get_history(product_name=None):

    conn = connect()

    if product_name:

        rows = conn.execute("""
            SELECT
                product_name,
                store,
                price,
                collected_at
            FROM observations
            WHERE product_name = ?
            ORDER BY collected_at
        """, (product_name,)).fetchall()

    else:

        rows = conn.execute("""
            SELECT
                product_name,
                store,
                price,
                collected_at
            FROM observations
            ORDER BY collected_at
        """).fetchall()

    conn.close()

    return rows
