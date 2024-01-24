#!/usr/bin/python3
def safe_print_division(a, b):
    """Function to return result of division of 2 int."""
    try:
        the_div = a / b
    except (TypeError, ZeroDivisionError):
        the_div = None
    finally:
        print("Inside result: {}".format(the_div))
    return (the_div)
