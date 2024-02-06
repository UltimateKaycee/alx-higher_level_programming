#!/usr/bin/python3
"""Function to write a text string to file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file

    Arguments are; filename and text: to write

    Will raise exception if file can't be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
