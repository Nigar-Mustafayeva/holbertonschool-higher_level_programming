#!/usr/bin/python3
"""
This is module documentation
"""


import json


def load_from_json_file(filename):
    """
    this is function documentation
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
