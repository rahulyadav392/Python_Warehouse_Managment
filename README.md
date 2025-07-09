# 📦 Inventory Management System (IMS)

A lightweight, mobile-friendly inventory tracking system using Python and Supabase designed to help warehouse staff and admins manage stock movements across two companies with centralized access. Built as a real-world project to support a transition into Data Analytics or Data Science.

---

## 🧠 Project Purpose

This project aims to:
- Digitize inventory transactions (Received / Dispatched / Returned)
- Provide a user-friendly method to log data/stock transactions by warehouse users with minimal tech skills
- Allow admins to approve, annotate, and track billing
- Unify stock data across two companies into one platform
- Serve as a strong portfolio project demonstrating Python, SQL, and data visualization skills

---

## 🧱 Tech Stack

| Area     | Tool              |
|----------|-------------------|
| UI       | Streamlit         |
| Backend  | Python             |
| Database | Supabase (PostgreSQL) |
| Auth     | Supabase Auth (planned) |
| Hosting  | Streamlit Cloud / Supabase |
| Reporting| Pandas, Excel/CSV export |

-- 📦 SKU Table
CREATE TABLE IF NOT EXISTS sku (
    sku_code INT PRIMARY KEY,           -- Manually entered primary key
    sku_name TEXT NOT NULL,              -- Product Name
    unit_price NUMERIC(10, 2),           -- Upto 2 Decimal places
    packing_size NUMERIC                 -- packing size (number)
);

---

## 🚀 Features

### 👷 Warehouse Person View

To Be Added

### 👨‍💼 Admin View

To Be Added

---

## 🧱 Project Scope
Let’s break the project into features:

📦 Products table: product name, category, unit price, SKU, etc.

🧍 Users/Roles: Admin and Warehouse Staff

📥 Stock In: record of received goods

📤 Stock Out: record of dispatched goods

🔁 Returns: optional, but useful for real-world use

📊 Live Inventory: compute current stock = stock in − stock out + returned

📑 Reports/Export: Excel or CSV download for stock summary
