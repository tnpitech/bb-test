from db import conn
from write_csv import write_csv_data

query = f"""
select il.lot_id, 
il.ingredient, 
count(distinct bi.batch_id) as batches_used,
count(distinct c.batch_id_on_pack) as batches_complained,
count(distinct case when bi.batch_id not in (
select batch_id
from batch_ingredients
where lot_id = 'L-01-04'
) and c.batch_id_on_pack is not null
then bi.batch_id end) as complained_without_L0104,
100 * count(distinct c.batch_id_on_pack) / count(distinct bi.batch_id) as complaint_percent
from ingredient_lots il 
inner join batch_ingredients bi on il.lot_id = bi.lot_id 
left join complaints c on bi.batch_id = c.batch_id_on_pack 
and c.symptom in ("ท้องเสียหลังรับประทาน", "รสขมผิดปกติ", "ปวดท้องรุนแรง", "คลื่นไส้อาเจียน", "กลิ่นหืนผิดปกติ")
where il.lot_id != "L-01-04"
group by il.lot_id 
having batches_complained > 0
order by complaint_percent desc
"""
rows = conn.execute(query).fetchall()
write_csv_data("output/ex2q2.csv", ["lot_id", "ingredient", "batches_used", "batches_used", "batches_complained", "complaint_without_L0104", "complaint_percent"], rows)
