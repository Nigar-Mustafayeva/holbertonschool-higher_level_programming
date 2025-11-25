#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and has a public method to print the list sorted.
"""


class MyList(list):
    """A list subclass with a method to print the list sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
