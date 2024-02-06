#!/usr/bin/python3
"""Function to read from a text file and print tostout"""


def read_file(filename=""):
    """Declaring function to read from a file

    Arguments are filename: filename

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
