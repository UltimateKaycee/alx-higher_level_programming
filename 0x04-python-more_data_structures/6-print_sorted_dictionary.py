#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function to print a dictionary by ordered keys."""
    [print("{}: {}".format(
                         o, a_dictionary[o])) for o in sorted(a_dictionary)]
