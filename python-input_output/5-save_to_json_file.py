#!/usr/bin/python3
"""
This is  module documentation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This is function documentation
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
