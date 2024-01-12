#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """To replace all occurrences of element by another in a list."""
    the_list = my_list[:]
    for start in range(len(the_list)):
        if the_list[start] == search:
            the_list[start] = replace
    return (the_list)
