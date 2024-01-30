#!/usr/bin/python3
"""Function for addition of integer."""

def add_integer(a, b=98):
    """Will return result of 2 integer addition.

    Will raise TypeError if neither args is integer nor float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
