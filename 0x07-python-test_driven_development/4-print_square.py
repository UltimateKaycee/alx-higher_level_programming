#!/usr/bin/python3
"""Module for a fuunction that prints square."""


def print_square(size):
    """Function to print square with # character.

    Arguments - size (int): height and width of square.
    Retruns TypeError if size is not integer and 
    returns ValueError if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for start in range(size):
        [print("#", end="") for move in range(size)]
        print("")
