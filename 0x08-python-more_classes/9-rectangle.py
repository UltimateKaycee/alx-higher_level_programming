#!/usr/bin/python3
"""A Class that Defines a Rectangle by another, 8."""


class Rectangle:
    """The rectangle class definition.

    Attributes are number_of_instances (int) of Rectangle and
        print_symbol (any) of the string symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Here, we initialize a the Rectangle.

        Arguments are width (int) of rectangle and
            height (int) of rectangle.
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
        """Getting and setting height rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """We return area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """We return perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """We return the bigger rectangle.

        Arguments are rect_1 (Rectangle) first Rectangle
        and rect_2 (Rectangle) second Rectangle.
        Will raise TypeError if either arguments is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """We return Rectangle of width == height == size.

        Arguments are size (int) that is width and height of Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """We return actual rectangle using # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for y in range(self.__height):
            [rectan.append(str(self.print_symbol)) for z in range(self.__width)]
            if y != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """We return string of rectangle."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """We print message of rectangle deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
