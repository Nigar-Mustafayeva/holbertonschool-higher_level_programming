#!/usr/bin/env python3
"""
Task 04: Extend dynamic product viewer to read from SQLite database (sql)
Supported sources:
    /products?source=json
    /products?source=csv
    /products?source=sql
Optional filtering:
    /products?source=sql&id=1
"""

import os
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------------------------------------------------------------
#  JSON READER
# ------------------------------------------------------------------------
def read_json_file(json_path):
    """Read products from a JSON file."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


# ------------------------------------------------------------------------
#  CSV READER
# ------------------------------------------------------------------------
def read_csv_file(csv_path):
    """Read CSV file and return list of dicts."""
    data = []
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                data.append(row)
        return data
    except Exception:
        return None


# ------------------------------------------------------------------------
#  SQLITE READER
# ------------------------------------------------------------------------
def read_sqlite_all(db_path):
    """Return all rows from SQLite database as list of dicts."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    except Exception:
        return None


def read_sqlite_by_id(db_path, product_id):
    """Return a single product by ID from SQLite."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()

        return dict(row) if row else None

    except Exception:
        return None


# ------------------------------------------------------------------------
#  FILE & TEMPLATE ENSURERS
# ------------------------------------------------------------------------
def ensure_data_files():
    """Ensure JSON, CSV, and SQLite DB are created if missing."""

    # JSON
    default_json = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
    ]

    if not os.path.exists("products.json"):
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(default_json, f, indent=4)

    # CSV
    if not os.path.exists("products.csv"):
        with open("products.csv", "w", encoding="utf-8") as f:
            f.write("id,name,category,price\n")
            f.write("1,Laptop,Electronics,799.99\n")
            f.write("2,Coffee Mug,Home Goods,15.99\n")

    # SQLite DB
    if not os.path.exists("products.db"):
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        cursor.execute("""
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        """)
        conn.commit()
        conn.close()


def ensure_template():
    """Ensure product_display.html exists."""
    template_path = "templates/product_display.html"
    if not os.path.exists("templates"):
        os.makedirs("templates")

    if not os.path.exists(template_path):
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(PRODUCT_TEMPLATE)


# ------------------------------------------------------------------------
#  FLASK ROUTE
# ------------------------------------------------------------------------
@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id")
    products = None
    error = None

    # Validate source
    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html",
                               error="Wrong source", products=None)

    # Fetch data depending on source
    if source == "json":
        products = read_json_file("products.json")

    elif source == "csv":
        products = read_csv_file("products.csv")

    elif source == "sql":
        if id_param:
            try:
                id_val = int(id_param)
                product = read_sqlite_by_id("products.db", id_val)
                if not product:
                    return render_template("product_display.html",
                                           error="Product not found", products=None)
                products = [product]
            except ValueError:
                return render_template("product_display.html",
                                       error="Invalid id format", products=None)
        else:
            products = read_sqlite_all("products.db")

    # Handle reading failure
    if products is None:
        return render_template("product_display.html",
                               error="Error reading data", products=None)

    # If id provided for json/csv, filter manually
    if id_param and source in ("json", "csv"):
        try:
            id_val = int(id_param)
            product = next((p for p in products if p["id"] == id_val), None)
            if not product:
                return render_template("product_display.html",
                                       error="Product not found", products=None)
            products = [product]
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid id format", products=None)

    return render_template("product_display.html",
                           products=products,
                           error=None)


# ------------------------------------------------------------------------
#  TEMPLATE (same as Task 3)
# ------------------------------------------------------------------------
PRODUCT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Display</title>
    <style>
        table { border-collapse: collapse; width: 50%; margin-top: 20px; }
        th, td { border: 1px solid #333; padding: 8px; text-align: left; }
        th { background-color: #f0f0f0; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Product List</h1>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% elif products %}
        <table>
            <tr>
                <th>Name</th>
                <th>Category</th>
                <th>Price ($)</th>
            </tr>
            {% for p in products %}
                <tr>
                    <td>{{ p.name }}</td>
                    <td>{{ p.category }}</td>
                    <td>{{ "%.2f"|format(p.price) }}</td>
                </tr>
            {% endfor %}
        </table>
    {% else %}
        <p>No products available.</p>
    {% endif %}
</body>
</html>
"""


# ------------------------------------------------------------------------

if __name__ == "__main__":
    ensure_data_files()
    ensure_template()
    app.run(debug=True, port=5000)

