#!/usr/bin/python3
"""
This module defines a function that returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: List of strings representing attributes and methods.
    """
    return dir(obj)
