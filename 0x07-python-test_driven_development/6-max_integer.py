#!/usr/bin/python3
"""A module that will find maximu int in a list
"""

def max_integer(list=[]):
    """A function that will find and return maximum int in list of ints
        function returns none if list is empty.
    """
    if len(list) == 0:
        return None
    output = list[0]
    start = 1
    while start < len(list):
        if list[start] > output:
            result = list[start]
        start += 1
    return output
