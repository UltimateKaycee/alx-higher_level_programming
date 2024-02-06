#!/usr/bin/python3
"""For function that returns an object of JSON string"""
import json


def from_json_string(my_str):
    """Declaring function to return object represented by JSON string

    Argument is my_str: JSON string

    """
    return json.loads(my_str)
