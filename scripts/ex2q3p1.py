from db import conn
from write_csv import write_csv_data

query = f"""
select bi.batch_id, bi.lot_id, pb.product_id, p.name as product_name
from batch_ingredients bi
left join production_batches pb on bi.batch_id = pb.batch_id
inner join products p on pb.product_id = p.product_id
where bi.lot_id = "L-01-04"
"""

rows = conn.execute(query).fetchall()
write_csv_data("output/ex2q3p1.csv", ["batch_id", "lot_id", "product_id", "product_name"], rows)
