#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """Base class for geometry operations"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer
        Args:
            name (str): name of the variable
            value (int): value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
