#!/usr/bin/python3
"""Module defining a MyList class that inherits from list."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending order without modifying original."""
        print(sorted(self))
