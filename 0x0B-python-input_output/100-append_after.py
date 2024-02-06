#!/usr/bin/python3
"""For Function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Defining function to appends line to file

    Arguments are filename: the filename
        search_string: the search string
        new_string: the string to insert

    """

    line_out = []
    with open(filename, 'r', encoding="utf-8") as f:
        for item in f:
            line_out += [item]
            if item.find(search_string) != -1:
                line_out += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(line_out))
