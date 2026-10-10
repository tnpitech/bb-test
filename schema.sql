CREATE TABLE suppliers (
    supplier_id TEXT PRIMARY KEY,
    name TEXT,
    main_ingredient TEXT,
    province TEXT
);
 
CREATE TABLE stores (
    store_id TEXT PRIMARY KEY,
    name TEXT,
    province TEXT
);
 
CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    name TEXT,
    shelf_life_days INTEGER
);
 
CREATE TABLE ingredient_lots (
    lot_id TEXT PRIMARY KEY,
    ingredient TEXT,
    supplier_id TEXT REFERENCES suppliers(supplier_id),
    received_date TEXT,
    qty_kg INTEGER,
    qc_result TEXT,
    storage_temp_c REAL
);
 
CREATE TABLE production_batches (
    batch_id TEXT PRIMARY KEY,
    product_id TEXT REFERENCES products(product_id),
    production_date TEXT,
    line_id TEXT,
    qty_units INTEGER
);
 
CREATE TABLE batch_ingredients (
    batch_id TEXT REFERENCES production_batches(batch_id),
    lot_id TEXT REFERENCES ingredient_lots(lot_id),
    qty_used_kg INTEGER
);
 
CREATE TABLE shipments (
    shipment_id TEXT PRIMARY KEY,
    batch_id TEXT REFERENCES production_batches(batch_id),
    store_id TEXT REFERENCES stores(store_id),
    ship_date TEXT,
    qty_units INTEGER
);
 
CREATE TABLE complaints (
    complaint_id TEXT PRIMARY KEY,
    complaint_date TEXT,
    store_id TEXT REFERENCES stores(store_id),
    product_id TEXT REFERENCES products(product_id),
    batch_id_on_pack TEXT REFERENCES production_batches(batch_id),
    symptom TEXT,
    channel TEXT
);
