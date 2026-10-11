from db import conn
from write_csv import write_csv_data

query = f"""
select bi.lot_id, bi.batch_id, sm.store_id, (
	select count(*)
    from complaints c
    where c.batch_id_on_pack = sm.batch_id
    and c.store_id = sm.store_id) as complaints
from batch_ingredients bi
join shipments sm on sm.batch_id = bi.batch_id
where bi.lot_id = 'L-01-04'
order by complaints desc;
"""

rows = conn.execute(query).fetchall()
write_csv_data("output/ex4.csv", ["lot_id", "batch_id", "store_id", "complained_count"], rows)
