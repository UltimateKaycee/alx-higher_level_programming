#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Function to return new dictionary with all values multipled by 2."""
    return ({m: a_dictionary[m] * 2 for m in a_dictionary})
