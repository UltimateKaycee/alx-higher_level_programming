#!/usr/bin/python3
"""Class definition that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class rectangle for BaseGeometry."""

    def __init__(self, width, height):
        """method initialization for rectangle.

        Argumemnts are width (int) of rectangle and height (int) of rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
