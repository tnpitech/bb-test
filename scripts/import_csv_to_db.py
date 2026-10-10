from pathlib import Path
import pandas as pd
from db import conn

project_dir = Path(__file__).resolve().parent.parent
SCHEMA_FILE = project_dir / "schema.sql"
DATA_DIR = project_dir / "Test/dataset/data"

TABLES = [
    "suppliers", "stores", "products", "ingredient_lots",
    "production_batches", "batch_ingredients", "shipments", "complaints",
]

conn.execute("PRAGMA foreign_keys = ON")

for table in reversed(TABLES):
    conn.execute(f"DROP TABLE IF EXISTS {table}")
with open(SCHEMA_FILE, encoding="utf-8") as f:
    conn.executescript(f.read())

for table in TABLES:
    df = pd.read_csv(f"{DATA_DIR}/{table}.csv")
    df.to_sql(table, conn, if_exists="append", index=False)
    print(f"{table}: {len(df)} แถว")

conn.commit()
conn.close()
