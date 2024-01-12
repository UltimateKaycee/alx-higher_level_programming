#!/usr/bin/python3

def uniq_add(my_list=[]):
    """That will add all unique integers once for each in a list."""
    final_list = 0
    for item in set(my_list):
        final_list += item
    return (final_list)
