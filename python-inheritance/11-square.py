#!/usr/bin/python3
"""
This is module documentation
"""


Rectangle = __import__('9-regtangle').Rectangle


class Square(Regtangle):
    """
    This is class documentation
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return f"[Square]{width}/{height}"
