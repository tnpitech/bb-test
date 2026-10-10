from .db import conn
from .write_csv import write_csv_data


def Question1p1(batch_id):
    print("Q1.1")
    query = f"""
    select bi.batch_id, il.lot_id, st.name
    from batch_ingredients bi
    inner join ingredient_lots il on bi.lot_id = il.lot_id
    inner join shipments sm on bi.batch_id = sm.batch_id
    inner join stores st on sm.store_id = st.store_id
    where bi.batch_id = "{batch_id}"
    order by bi.lot_id ASC
    """
    rows = conn.execute(query).fetchall()
    for row in rows:
        lot_id = row["lot_id"]
        store_name = row["name"]
        print(f"ล็อตผลิต {batch_id} ใช้วัตถุดิบล็อต {lot_id} ถูกส่งไปร้าน {store_name}")
    write_csv_data("output/ex1q1p1.csv", ["batch_id", "lot_id", "store_name"], rows)

def Question1p2(ing_lot_id):
    print("Q1.2")
    query = f"""
    select SUM(qty_used_kg) as total_used_kg, COUNT(batch_id) AS batches
    from batch_ingredients
    where lot_id = "{ing_lot_id}"
    """

    row = conn.execute(query).fetchone()
    total_used_kg = row["total_used_kg"]
    batches = row["batches"]
    print(f"วัตถุดิบล็อต {ing_lot_id} ถูกใช้ไปทั้งหมด {total_used_kg} กิโลกรัม ในล็อตผลิต {batches} ล็อต")
    write_csv_data("output/ex1q1p2.csv", ["total_used_kg", "batches"], [[total_used_kg, batches]])

def Question1p3():
    print("Q1.3")
    query = f"""
    select st.store_id, st.name as store_name, COUNT(c.complaint_id) as complaint_count 
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
