"""Daily public-catalogue collector for GitHub Actions."""
import csv
from datetime import datetime, timezone
from pathlib import Path
from scrapers.lulu import collect_lulu

OUTPUT = Path("data/pricescout_history.csv")
FIELDS = ["product_name", "store", "price", "collected_at", "source_url"]

def main():
    products = collect_lulu()
    valid = [p for p in products if p.get("product_name") and p.get("store") and p.get("price") is not None]
    if not valid:
        raise RuntimeError("No valid public catalogue products returned; refusing to write fake history.")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    existing, seen = [], set()
    if OUTPUT.exists():
        with OUTPUT.open("r", newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                existing.append(row)
                seen.add((row.get("product_name"), row.get("store"), (row.get("collected_at") or "")[:10]))

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    added = 0
    for product in valid:
        stamp = product.get("collected_at") or now
        key = (product["product_name"], product["store"], stamp[:10])
        if key in seen:
            continue
        existing.append({
            "product_name": product["product_name"],
            "store": product["store"],
            "price": f'{float(product["price"]):.3f}',
            "collected_at": stamp,
            "source_url": product.get("source_url") or "",
        })
        seen.add(key)
        added += 1

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(existing)
    print(f"Valid catalogue products: {len(valid)}; new daily observations: {added}; total history rows: {len(existing)}")

if __name__ == "__main__":
    main()
