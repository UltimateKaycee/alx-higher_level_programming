#!/usr/bin/python3
"""We define class called Square."""


class Square:
    """The square class."""

    def __init__(self, size=0):
        """The Square class is initialized.

            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("should be integer")
        elif size < 0:
            raise ValueError("should be gt or equal 0")
        self.__size = size

    def area(self):
        """return area of square."""
        return (self.__size * self.__size)
