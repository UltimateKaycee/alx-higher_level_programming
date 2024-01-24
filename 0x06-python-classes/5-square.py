#!/usr/bin/python3
"""We define class named Square."""


class Square:
    """Here, our square class."""

    def __init__(self, size):
        """We get Square initialized.

            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """Let's get and set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("should be integer")
        elif value < 0:
            raise ValueError("should be gt or equal 0")
        self.__size = value

    def area(self):
        """return area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Output square with # symbol."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
