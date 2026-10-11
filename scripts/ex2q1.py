from db import conn
from write_csv import write_csv_data

query = f"""
select il.lot_id,
il.ingredient,
count(distinct bi.batch_id) as batches_used,
count(distinct c.batch_id_on_pack) as batches_complained,
100 * count(distinct c.batch_id_on_pack) / count(distinct bi.batch_id) as complaint_percent
from ingredient_lots il
inner join batch_ingredients bi on il.lot_id = bi.lot_id
left join complaints c on bi.batch_id = c.batch_id_on_pack
and c.symptom in ("ท้องเสียหลังรับประทาน", "รสขมผิดปกติ", "ปวดท้องรุนแรง", "คลื่นไส้อาเจียน", "กลิ่นหืนผิดปกติ")
group by il.lot_id
order by complaint_percent desc
"""
rows = conn.execute(query).fetchall()
for row in rows:
    lot_id = row["lot_id"]
    ing = row["ingredient"]
    batches_used = row["batches_used"]
    batches_complained = row["batches_complained"]
    complaint_percent = row["complaint_percent"]
write_csv_data("output/ex2q1.csv", ["lot_id", "ingredient", "batches_used", "batches_used", "batches_complained", "complaint_percent"], rows)
