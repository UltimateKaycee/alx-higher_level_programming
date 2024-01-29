#!/usr/bin/python3
"""A Class for the definition of a Rectangle by another, 7."""


class Rectangle:
    """A rectangle class with Attributes, number_of_instances (int) of
    Rectangle and print_symbol (any) of string output.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Here, we initialize a rectangle.

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
        """Here, we return area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Here, perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """output the bigger rectangle.

        Arguments are rect_1 (Rectangle) first Rectangle and
            rect_2 (Rectangle) second Rectangle.
        TypeError occurs if either arguments isn't a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """We return printed rectangle with # char.
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
        """We return string of rectangle."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """We print message of deletion of Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
