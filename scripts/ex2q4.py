from db import conn
from write_csv import write_csv_data

query = f"""
select c.store_id, st.name as store_name ,count(*) as complained_count
from complaints c
inner join stores st on st.store_id = c.store_id 
where c.symptom in ("ท้องเสียหลังรับประทาน", "รสขมผิดปกติ", "ปวดท้องรุนแรง", "คลื่นไส้อาเจียน", "กลิ่นหืนผิดปกติ")
and c.batch_id_on_pack is not null
and c.batch_id_on_pack not in (
	select batch_id
	from batch_ingredients
	where lot_id = "L-01-04"
)
group by c.store_id
order by complained_count desc
"""

rows = conn.execute(query).fetchall()
write_csv_data("output/ex2q4.csv", ["store_id", "store_name", "complained_count"], rows)
