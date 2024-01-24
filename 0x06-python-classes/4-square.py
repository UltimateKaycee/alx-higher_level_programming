#!/usr/bin/python3
"""We define a Square class."""


class Square:
    """Our Square class."""

    def __init__(self, size=0):
        """Square is initialized.

            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """We do get and set of size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("should be integer")
        elif value < 0:
            raise ValueError("should be gt or equal 0")
        self.__size = value

    def area(self):
        """We return area of square."""
        return (self.__size * self.__size)
