#!/usr/bin/python3
"""
This module defines a Rectangle class.

The Rectangle class includes private width and height attributes
with property getters and setters that validate the input.
It can be used to create and manage rectangle objects.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Private instance attributes:
        __width (int): The width of the rectangle (must be >= 0)
        __height (int): The height of the rectangle (must be >= 0)

    Properties:
        width (int): Getter and setter for the width attribute.
        height (int): Getter and setter for the height attribute.

    The setters raise exceptions if values are not integers
    or are less than 0.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height
