#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print out all the integers in a list."""
    for start in range(len(my_list)):
        print("{:d}".format(my_list[start]))
