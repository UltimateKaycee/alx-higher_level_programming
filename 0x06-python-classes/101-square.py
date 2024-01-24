#!/usr/bin/python3
"""Let's begin with class named Square."""


class Square:
    """Here, our square class."""

    def __init__(self, size=0, position=(0, 0)):
        """our square class initialized.

            size (int): size of new square.
            position (int, int): position of new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """let's get and set size of square class."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("should be integer")
        elif value < 0:
            raise ValueError("should be gt or equal 0")
        self.__size = value

    @property
    def position(self):
        """We get and set position of square class."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position should 2 integers")
        self.__position = value

    def area(self):
        """We return area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Output square with # symbol."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """We define print() of Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
