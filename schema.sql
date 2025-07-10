-- 📦 SKU Table
CREATE TABLE IF NOT EXISTS sku (
    sku_code INT PRIMARY KEY,
    sku_name TEXT NOT NULL,
    unit_price NUMERIC(10, 2),
    packing_size NUMERIC,
    user_id UUID REFERENCES auth.users(id)
);

-- 📥 Stock In Table
CREATE TABLE IF NOT EXISTS stock_in (
    in_id SERIAL PRIMARY KEY,
    sku_code INT REFERENCES sku(sku_code),
    quantity INT,
    received_date DATE DEFAULT CURRENT_DATE,
    bill_number_in INT,
    vehicle_number_in TEXT,
    approved BOOLEAN DEFAULT FALSE,
    user_id UUID REFERENCES auth.users(id)
);

-- 📤 Stock Out Table
CREATE TABLE IF NOT EXISTS stock_out (
    out_id SERIAL PRIMARY KEY,
    sku_code INT REFERENCES sku(sku_code),
    quantity INT,
    dispatched_date DATE DEFAULT CURRENT_DATE,
    bill_number_out INT,
    vehicle_number_out TEXT,
    tpt_name TEXT,
    approved BOOLEAN DEFAULT FALSE,
    user_id UUID REFERENCES auth.users(id)
);

-- 🔁 Returns Table
CREATE TABLE IF NOT EXISTS returns (
    return_id SERIAL PRIMARY KEY,
    sku_code INT REFERENCES sku(sku_code),
    quantity INT,
    return_date DATE DEFAULT CURRENT_DATE,
    reason TEXT,
    approved BOOLEAN DEFAULT FALSE,
    user_id UUID REFERENCES auth.users(id)
);

-- 👥 Users Table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    role TEXT CHECK (role IN ('admin', 'staff')),
    user_id UUID UNIQUE REFERENCES auth.users(id)
);
