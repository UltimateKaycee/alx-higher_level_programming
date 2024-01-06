#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """To print out all the ints in a list, reversed."""
    if myTake(my_list, list):
        my_list.reverse()
        for start in my_list:
            print("{:d}".format(start))
