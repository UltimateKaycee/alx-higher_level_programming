#!/usr/bin/python3
"""Class to define a Rectangle based on another."""


class Rectangle:
    """The rectangle class definition."""

    def __init__(self, width=0, height=0):
        """We initialize the new Rectangle class.

        Arguments are width (int) of new rectangle and
            height (int) of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """We get/set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """We get/set height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """result is area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """result is perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
