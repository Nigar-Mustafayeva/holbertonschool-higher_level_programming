#!/usr/bin/python3
# 1-my_list.py

class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
