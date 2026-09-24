"""Loads test data from CSV files in the /data folder."""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_csv(filename: str) -> list:
    """Return a list of dicts, one per CSV row.

    encoding="utf-8-sig" silently removes the invisible BOM character that
    Excel on Windows adds when you "Save as CSV" - without it the first
    column name would be corrupted.
    """
    path = DATA_DIR / filename
    with open(path, newline="", encoding="utf-8-sig") as file:
        rows = []
        for row in csv.DictReader(file):
            if not any((value or "").strip() for value in row.values()):
                continue  # skip completely blank lines
            rows.append({key.strip(): (value or "").strip() for key, value in row.items()})
        return rows
