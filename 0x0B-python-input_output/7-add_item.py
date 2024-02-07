#!/usr/bin/python3
"""Script to aAdd all arguments to Python list and save them to a file.
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
            '6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        elements = load_from_json_file("add_item.json")
    except:
        pass
        elements = []
    for c in argv[1:]:
        elements.append(c)
    save_to_json_file(elements, "add_item.json")
