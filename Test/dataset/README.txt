ชุดข้อมูล Take-home — ตามหาล็อตวัตถุดิบที่มีปัญหา
=================================================
ข้อมูลทั้งหมดเป็นข้อมูลสมมติเพื่อการทดสอบ
โจทย์ฉบับเต็มอยู่ในไฟล์ "โจทย์ Take-home ฉบับนักศึกษา - ตามหาล็อตวัตถุดิบ (สำหรับผู้สมัคร).html"

data/
  suppliers.csv          ซัพพลายเออร์ (supplier_id, name, main_ingredient, province)
  ingredient_lots.csv    ล็อตวัตถุดิบที่รับเข้า (lot_id, ingredient, supplier_id, received_date, qty_kg, qc_result, storage_temp_c)
  products.csv           สินค้า (product_id, name, shelf_life_days)
  production_batches.csv ล็อตผลิต (batch_id, product_id, production_date, line_id, qty_units)
  batch_ingredients.csv  ตารางเชื่อม ล็อตผลิต ↔ ล็อตวัตถุดิบ (batch_id, lot_id, qty_used_kg)
  shipments.csv          การจัดส่ง (shipment_id, batch_id, store_id, ship_date, qty_units)
  stores.csv             ร้านค้า (store_id, name, province)
  complaints.csv         ข้อร้องเรียน (complaint_id, complaint_date, store_id, product_id, batch_id_on_pack [อาจว่าง], symptom, channel)

docs/
  01_บันทึก_QA_สรุปข้อร้องเรียน.txt
  02_รายงานตรวจสอบหน้าร้าน_ST07.txt
  03_ใบส่งมอบวัตถุดิบ_กะทิผง_S01.txt
  04_สรุปข้อร้องเรียนบรรจุภัณฑ์.txt
  (แต่ละเอกสารแบ่งย่อหน้าด้วย [ย่อหน้า n] เพื่อใช้อ้างอิง)

CSV เข้ารหัส UTF-8 (มี BOM) · วันที่เป็น ค.ศ. รูปแบบ YYYY-MM-DD
