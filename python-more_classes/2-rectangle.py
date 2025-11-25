#!/usr/bin/python3
"""
This module defines a Rectangle class.

The Rectangle class has private width and height attributes,
property getters and setters with validation, and methods
to compute area and perimeter.
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

    Public methods:
        area(): Returns the rectangle area.
        perimeter(): Returns the rectangle perimeter.
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
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

