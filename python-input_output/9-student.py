#!/usr/bin/python3
"""
This is module documentation
"""


class Student:
    """
    This is class documentation
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__.copy()
