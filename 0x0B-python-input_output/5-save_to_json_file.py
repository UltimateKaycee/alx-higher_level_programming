#!/usr/bin/python3
"""For function that writes Object to text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """Declaring function to write object to file with JSON

    Arguments are my_obj: object and filename: name of textfile

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
