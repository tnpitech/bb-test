from db import conn
from write_csv import write_csv_data

query = f"""
select st.store_id, st.name as store_name, p.name as product_name, SUM(sm.qty_units) as total_units
from stores st
inner join shipments sm on st.store_id = sm.store_id
inner join batch_ingredients bi  on sm.batch_id = bi.batch_id
inner join production_batches pb on sm.batch_id = pb.batch_id 
inner join products p on pb.product_id = p.product_id 
where bi.lot_id = "L-01-04"
group by st.store_id
order by total_units desc
"""

rows = conn.execute(query).fetchall()
write_csv_data("output/ex2q3p2.csv", ["store_id", "store_name", "product_name", "total_units"], rows)
