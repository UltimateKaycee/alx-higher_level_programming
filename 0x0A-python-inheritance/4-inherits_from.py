#!/usr/bin/python3
"""Function for checking inherited class."""


def inherits_from(obj, a_class):
    """Will checks if obj is inherited class.

    Arguments are obj (any) object to check and a_class (type) to match.
    Returns True if found and False, if not.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
