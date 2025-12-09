#!/usr/bin/env python3
"""
Task 03: Read from JSON/CSV and dynamically display using Flask.
Supports:
  /products?source=json
  /products?source=csv
  /products?source=json&id=2
"""

import os
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------------------------------------------------
# Utility functions
# ------------------------------------------------------------

def read_json_file(json_path):
    """Read products from a JSON file."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)  # returns a list of dicts
    except Exception:
        return None


def read_csv_file(csv_path):
    """Read products from a CSV file and convert to list of dicts."""
    data = []
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to correct types
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                data.append(row)
        return data
    except Exception:
        return None


# ------------------------------------------------------------
# Ensure data files and template exist
# ------------------------------------------------------------

def ensure_data_files():
    """Create products.json and products.csv if missing."""
    default_json = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
    ]

    if not os.path.exists("products.json"):
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(default_json, f, indent=4)

    if not os.path.exists("products.csv"):
        with open("products.csv", "w", encoding="utf-8") as f:
            f.write("id,name,category,price\n")
            f.write("1,Laptop,Electronics,799.99\n")
            f.write("2,Coffee Mug,Home Goods,15.99\n")


def ensure_template():
    """Create product_display.html template if missing."""
    template_path = "templates/product_display.html"
    if not os.path.exists("templates"):
        os.makedirs("templates")

    if not os.path.exists(template_path):
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(PRODUCT_TEMPLATE)


# ------------------------------------------------------------
# Route
# ------------------------------------------------------------

@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id", None)

    error_msg = None
    products = None

    # 1. Validate source
    if source not in ("json", "csv"):
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # 2. Read data depending on source
    if source == "json":
        products = read_json_file("products.json")
    else:
        products = read_csv_file("products.csv")

    if products is None:
        return render_template("product_display.html",
                               error="Error reading data file",
                               products=None)

    # 3. If id is provided, filter products
    if id_param:
        try:
            id_param = int(id_param)
            product = next((p for p in products if p["id"] == id_param), None)
            if not product:
                return render_template("product_display.html",
                                       error="Product not found",
                                       products=None)
            products = [product]  # Display single product
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid id format",
                                   products=None)

    # 4. Render normally
    return render_template("product_display.html",
                           products=products,
                           error=None)


# ------------------------------------------------------------
# Template content
# ------------------------------------------------------------

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

# ------------------------------------------------------------

if __name__ == "__main__":
    ensure_data_files()
    ensure_template()
    app.run(debug=True, port=5000)
