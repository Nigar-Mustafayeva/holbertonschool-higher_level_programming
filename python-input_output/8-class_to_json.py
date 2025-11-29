#!/usr/bin/python3
"""
Module that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary of all attributes of an object.
    Args:
        obj: Instance of a class.
    Returns:
        dict: A dictionary with all the attributes of obj.
    """
    return obj.__dict__.copy()
