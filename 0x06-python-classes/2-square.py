#!/usr/bin/python3
"""We define a class named Square."""


class Square:
    """The square class."""

    def __init__(self, size=0):
        """The Square class is initialized.

            size (int): size of square.
        """
        if not isinstance(size, int):
            raise TypeError("must be integer")
        elif size < 0:
            raise ValueError("size should gt or equal 0")
        self.__size = size
