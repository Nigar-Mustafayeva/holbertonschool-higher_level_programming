#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them as JSON in add_item.json
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Step 1: Load existing list, or create empty list if file doesn't exist
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Step 2: Add all command-line arguments
items.extend(sys.argv[1:])

# Step 3: Save updated list back to file
save_to_json_file(items, filename)
