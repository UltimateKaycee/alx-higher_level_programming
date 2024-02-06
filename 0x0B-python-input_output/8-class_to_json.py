#!/usr/bin/python3
"""For a function that returns dictionary description with simple
data structure (list, dict, str, int, bool) for a JSON serialization of an object
"""


def class_to_json(obj):
    """Declaring function to return dict description of object"""

    the_output = {}
    if hasattr(obj, "__dict__"):
        the_output = obj.__dict__.copy()
    return the_output
