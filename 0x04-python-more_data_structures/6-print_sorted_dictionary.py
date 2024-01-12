#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function to print a dictionary by ordered keys."""
    [print("{}: {}".format(order, a_dictionary[order])) for order in sorted(a_dictionary)]
