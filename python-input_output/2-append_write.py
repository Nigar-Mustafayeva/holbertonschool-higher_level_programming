#!/usr/bin/python3
"""
This is module documentation
"""


def append_write(filename="", text=""):
    """
    This is function documentation
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
