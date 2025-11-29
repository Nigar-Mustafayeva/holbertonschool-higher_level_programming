#!/usr/bin/env python3
"""
Basic serialization module
This module provides functions to:
1. Serialize a Python dictionary to a JSON file.
2. Deserialize a JSON file back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Output JSON file name
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)  # convert dict to JSON and save to file


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary.
    Args:
        filename (str): Input JSON file name
    Returns:
        dict: Python dictionary deserialized from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)  # read JSON and convert to dict
    return data

