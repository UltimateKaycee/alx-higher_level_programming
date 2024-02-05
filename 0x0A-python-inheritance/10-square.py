#!/usr/bin/python3
"""Class definition for square that inherits from rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class that inherits."""

    def __init__(self, size):
        """Will initialize square class.

        Arguments are size (int) the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
