#!/usr/bin/python3
"""Class definition for rectangle which inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition for rectangle for BaseGeometry."""

    def __init__(self, width, height):
        """Function intialization.

        Arguments are width (int) of new Rectangle and height (int).
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Function will output area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Will return print() and str() returns rectangle description."""
        the_string = "[" + str(self.__class__.__name__) + "] "
        the_string += str(self.__width) + "/" + str(self.__height)
        return the_string
