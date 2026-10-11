from db import conn
from write_csv import write_csv_data

print("Q1.3")
query = f"""
select st.store_id, st.name as store_name, count(c.complaint_id) as complaint_count 
from stores st
inner join complaints c on st.store_id = c.store_id 
where c.symptom in ("ปวดท้องรุนแรง", "คลื่นไส้อาเจียน", "กลิ่นหืนผิดปกติ", "รสขมผิดปกติ", "ท้องเสียหลังรับประทาน")
group by st.store_id
order by complaint_count DESC
"""

rows = conn.execute(query).fetchall()
for row in rows:
    store_id = row["store_id"]
    store_name = row["store_name"]
    complaint_count = row["complaint_count"]
    print(f"{store_name} มีข้อร้องเรียนที่เป็นอาการเจ็บป่วยหรือกลิ่น/รสผิดปกติ(ไม่นับเรื่องบรรจุภัณฑ์) {complaint_count} รายการ")
write_csv_data("output/ex1q1p3.csv", ["store_id", "name", "complaint_count"], rows)
