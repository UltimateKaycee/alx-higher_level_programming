#!/usr/bin/python3
"""Square class is defined."""


class Square:
    """here, the square."""

    def __init__(self, size=0):
        """Square class is Initialized.

           size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """We get and set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size should be integer")
        elif value < 0:
            raise ValueError("size should be gt or equal 0")
        self.__size = value

    def area(self):
        """let's return area of square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Here we define == comparator to Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Here, we define != comparator to Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """here, we define < comparator to Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Here, we define <= comparator to Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Here, we define > comparator to Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Here, we define >= comparator to Square."""
        return self.area() >= other.area()
