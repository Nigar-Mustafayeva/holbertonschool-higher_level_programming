"""
task_02_logic.py

Flask app extension for Task 02: Jinja logic (loops and conditionals).

This file adds a /items route that reads items.json and renders
templates/items.html which demonstrates Jinja's {% for %} loop and
{% if %} conditional to display a list or a "No items found" message.

Run:
    python task_02_logic.py

Then open http://127.0.0.1:5000/items
"""

import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)

# Template content for items.html
ITEMS_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Items List</title>
</head>
<body>
    {% include 'header.html' %}

    <main>
        <h1>Items List</h1>

        {% if items and items | length > 0 %}
            <ul>
            {% for it in items %}
                <li>{{ it }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No items found</p>
        {% endif %}

    </main>

    {% include 'footer.html' %}
</body>
</html>
"""

# Default JSON data
DEFAULT_ITEMS = {"items": ["Python Book", "Flask Mug", "Jinja Sticker"]}


def ensure_templates_and_data():
    """Ensure templates/ exists and items.json + items.html are present."""
    templates_dir = 'templates'
    if not os.path.isdir(templates_dir):
        os.makedirs(templates_dir, exist_ok=True)

    items_html_path = os.path.join(templates_dir, 'items.html')
    if not os.path.exists(items_html_path):
        with open(items_html_path, 'w', encoding='utf-8') as f:
            f.write(ITEMS_TEMPLATE)

    # Ensure items.json exists
    json_path = 'items.json'
    if not os.path.exists(json_path):
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_ITEMS, f, indent=4)


@app.route('/items')
def items():
    json_path = 'items.json'
    if not os.path.exists(json_path):
        # In production you might want to return a 404 or a default page.
        abort(404, description='Data file not found')

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        # If JSON is malformed or unreadable, respond with 500
        abort(500, description=f'Error reading data file: {e}')

    items_list = data.get('items') if isinstance(data, dict) else None

    # Ensure we pass a list (or empty list) to the template
    if not isinstance(items_list, list):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    ensure_templates_and_data()
    app.run(debug=True, port=5000)
