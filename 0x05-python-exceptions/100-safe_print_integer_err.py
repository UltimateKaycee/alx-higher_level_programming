#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Function to print integer with "{:d}".format().

    Arguments:
        value (int): The integer.

    Will return False if a TypeError or ValueError
    occurs otherwise, True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
