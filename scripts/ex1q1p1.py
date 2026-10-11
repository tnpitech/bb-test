from db import conn
from write_csv import write_csv_data

BATCH_ID = "B0028"

print("Q1.1")
query = f"""
select bi.batch_id, il.lot_id, st.name
from batch_ingredients bi
inner join ingredient_lots il on bi.lot_id = il.lot_id
inner join shipments sm on bi.batch_id = sm.batch_id
inner join stores st on sm.store_id = st.store_id
where bi.batch_id = "{BATCH_ID}"
order by bi.lot_id ASC
"""
rows = conn.execute(query).fetchall()
for row in rows:
    lot_id = row["lot_id"]
    store_name = row["name"]
    print(f"ล็อตผลิต {BATCH_ID} ใช้วัตถุดิบล็อต {lot_id} ถูกส่งไปร้าน {store_name}")
write_csv_data("output/ex1q1p1.csv", ["batch_id", "lot_id", "store_name"], rows)
