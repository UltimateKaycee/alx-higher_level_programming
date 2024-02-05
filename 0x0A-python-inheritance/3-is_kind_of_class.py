#!/usr/bin/python3
"""Function to check for class inheritance for a class."""


def is_kind_of_class(obj, a_class):
    """Will check if object is instance of or inherited instance of class.

    Arguments are obj (any) object to check and a_class (type) to match obj to.
    Returns True if matched, else, False.
    """
    if isinstance(obj, a_class):
        return True
    return False
