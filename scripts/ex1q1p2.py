from db import conn
from write_csv import write_csv_data

ING_LOT_ID = "L-01-04"

print("Q1.2")
query = f"""
select SUM(qty_used_kg) as total_used_kg, COUNT(batch_id) AS batches
from batch_ingredients
where lot_id = "{ING_LOT_ID}"
"""

row = conn.execute(query).fetchone()
total_used_kg = row["total_used_kg"]
batches = row["batches"]
print(f"วัตถุดิบล็อต {ING_LOT_ID} ถูกใช้ไปทั้งหมด {total_used_kg} กิโลกรัม ในล็อตผลิต {batches} ล็อต")
write_csv_data("output/ex1q1p2.csv", ["total_used_kg", "batches"], [[total_used_kg, batches]])
