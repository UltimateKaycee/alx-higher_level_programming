#!/usr/bin/python3
def safe_print_integer(value):
    """Function to print integer with "{:d}".format().

       value (int): The integer.

       Will return False if TypeError or ValueError occurs
       Otherwise returns True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
