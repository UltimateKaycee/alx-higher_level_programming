#!/usr/bin/python3
"""For a function that returns the JSON of an object
"""
import json


def to_json_string(my_obj):
    """Declaring function to returns the JSON rep of object

    Arguments are my_obj: object

"""
    return json.dumps(my_obj)
