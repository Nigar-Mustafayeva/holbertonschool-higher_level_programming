#!/usr/bin/env python3
"""
CSV to JSON conversion module
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.
    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion successful, False otherwise.
    """
    try:
        # Read CSV file
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]  # List of dictionaries

        # Write JSON file
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # CSV file not found
        return False
    except Exception:
        # Any other error (e.g., malformed file)
        return False
