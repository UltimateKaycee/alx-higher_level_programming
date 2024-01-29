#!/usr/bin/python3
"""A Class that defines a rectangle based on another."""


class Rectangle:
    """A rectangle class definition."""

    def __init__(self, width=0, height=0):
        """We initialize the new Rectangle class.

        Argsuments are width (int) of our new rectangle.
            and height (int) of our new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting and setting width of rectangle."""
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
        """Getting and seting height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
