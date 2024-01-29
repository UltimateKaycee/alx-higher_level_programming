#!/usr/bin/python3
"""A Class that defines a rectangle by another 5."""


class Rectangle:
    """Class definition with attributes of number_of_instances (int)
    of rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Here, we initialize the rectangle.

        Arguments are width (int) of the rectangle and
        height (int) of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Geting and setting width of rectangle."""
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
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Output area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Output perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Computer the string of the rectangle using # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for gba in range(self.__height):
            [rectan.append('#') for wepu in range(self.__width)]
            if gba != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """Output string of rectangle."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """Print message of deletion of rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
