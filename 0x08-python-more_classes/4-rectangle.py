#!/usr/bin/python3
"""A Class that defines a rectangle."""


class Rectangle:
    """The rectangle class definition."""

    def __init__(self, width=0, height=0):
        """Here is initializing the rectangle.

        Arguments are width (int) of the rectangle and
            height (int) height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting and setting width of Rectangle."""
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
        """Getting and setting height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """outputing area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """we return perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """output the actual rectangle using # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for start in range(self.__height):
            [rectan.append('#') for run in range(self.__width)]
            if start != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """output string of rectangle."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)
