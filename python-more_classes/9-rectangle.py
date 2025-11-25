#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height, and instance count.

Features:
- Private attributes with validation
- Class attributes: number_of_instances and print_symbol
- Area and perimeter methods
- String representation using print_symbol
- Repr to recreate instance using eval()
- Message when an instance is deleted
- Static method bigger_or_equal to compare rectangles by area
- Class method square to create a square rectangle
"""


class Rectangle:
    """
    Represents a rectangle.

    Class Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.

    Private instance attributes:
        __width (int)
        __height (int)

    Methods:
        area(): Returns area
        perimeter(): Returns perimeter
        __str__(): Prints rectangle with print_symbol
        __repr__(): Returns string to recreate instance
        __del__(): Prints deletion message
        bigger_or_equal(): Static method to compare two rectangles by area
        square(): Class method to create a square rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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
        """Return a string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        return "\n".join([line for _ in range(self.__height)])

    def __repr__(self):
        """Return a string to recreate the rectangle via eval()."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted and update counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area.

        If both areas are equal, return rect_1.

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
