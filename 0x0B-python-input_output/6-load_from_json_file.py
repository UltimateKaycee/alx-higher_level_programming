#!/usr/bin/python3
"""For function that creates an Object from JSON file
"""
import json


def load_from_json_file(filename):
    """Declaring a function to create Object from JSON file

    Argument is filename: name of textfile
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
