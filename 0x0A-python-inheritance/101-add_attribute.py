#!/usr/bin/python3
"""Function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Function definition for new attribute.

    Arguments are obj (any), att (str) the
    attribute to add and value (any) of attri.
    Raises TypeError if attrib can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
