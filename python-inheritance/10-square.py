#!/usr/bin/python3
"""
This is module documentation
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is class documentation
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
