#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Function to delete key with a particular value in dictionary."""
    while value in a_dictionary.values():
        for c, d in a_dictionary.items():
            if d == value:
                del a_dictionary[c]
                break

    return (a_dictionary)
