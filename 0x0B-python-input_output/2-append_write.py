#!/usr/bin/python3
"""For function that appends string to text file
"""


def append_write(filename="", text=""):
    """Declaring fFunction to append string

    Arguments are: filename, and text - to write

    Will raise exception if file can't be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
