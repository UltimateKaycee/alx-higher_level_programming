#!/usr/bin/python3
"""Let's define a MagicClass for python bytecode."""

import math


class MagicClass:
    """Here, our circle."""

    def __init__(self, radius=0):
        """Our MagicClass initialized.
           radius (float or int): radius
           of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius should be number")
        self.__radius = radius

    def area(self):
        """We return area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """We return circumference of circle MagicClass."""
        return (2 * math.pi * self.__radius)
