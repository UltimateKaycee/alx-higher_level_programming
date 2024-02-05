#!/usr/bin/python3
"""Function to check for a class."""


def is_same_class(obj, a_class):
    """Will check if object is instance of class.

    Argument are obj (any): to check and a_class (type): to check for.
    Returns True if obj is instance of a_class, else, False.
    """
    if type(obj) == a_class:
        return True
    return False
