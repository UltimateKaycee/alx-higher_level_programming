#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """A function which safely executes a function.

    Arguments:
        fct: The function.
        args: the arguments of the function.

    Will returns None if an error occurs,
        Otherwise, result of the function call.
    """
    try:
        the_result = fct(*args)
        return (the_result)
    except Exception as dead:
        print("Exception: {}".format(dead), file=sys.stderr)
        return (None)
