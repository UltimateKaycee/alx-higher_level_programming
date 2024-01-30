#!/usr/bin/python3
"""Module for a function that prints name."""


def say_my_name(first_name, last_name=""):
    """Function to print a name.

    Arguments:
        first_name (str): First name.
        last_name (str): Last name.
    Returns TypeError if neither inputs are string type.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
