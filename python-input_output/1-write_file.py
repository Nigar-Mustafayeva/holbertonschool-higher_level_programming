#!/usr/bin/python3
"""
This is module documentation
"""


def write_file(filename="", text=""):
    """
    This is function documentation
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
