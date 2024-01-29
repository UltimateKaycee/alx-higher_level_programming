#!/usr/bin/python3
"""A Class that defines a rectangle by another, 6."""


class Rectangle:
    """A rectangle class definition with Attributes as
        number_of_instances (int) of rectangle and
        print_symbol (any) as symbol for string.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        """Returns area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """outputs actual rectangle with # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for v in range(self.__height):
            [rectan.append(str(self.print_symbol)) for w in range(self.__width)]
            if v != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """returns string of rectangle."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """prints message of deletion of rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
