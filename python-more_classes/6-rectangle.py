#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height, and instance tracking.

Features:
- Private attributes with validation
- Area and perimeter methods
- String representation with '#'
- Repr to recreate instance using eval()
- Class attribute number_of_instances
- Message when an instance is deleted
"""


class Rectangle:
    """
    Represents a rectangle.

    Class Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.

    Private instance attributes:
        __width (int)
        __height (int)

    Methods:
        area(): Returns area
        perimeter(): Returns perimeter
        __str__(): Prints rectangle with '#'
        __repr__(): Returns string to recreate instance
        __del__(): Prints deletion message
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string to recreate the rectangle via eval()."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted and update counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
