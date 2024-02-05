#!/usr/bin/python3
"""Class definition for square that inherits from rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition for our square."""

    def __init__(self, size):
        """Function to initialize our new square.

        Arguments are size (int) of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
