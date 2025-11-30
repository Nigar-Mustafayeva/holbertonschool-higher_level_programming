#!/usr/bin/python3
"""
Module: 1-my_list
Defines a class MyList that inherits from list
and adds a public method to print the list in sorted order.
"""


class MyList(list):
    """
    Class MyList inherits from the built-in list.
    Public Methods:
        - print_sorted(): prints the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying
        the original list.
        """
        print(sorted(self))
