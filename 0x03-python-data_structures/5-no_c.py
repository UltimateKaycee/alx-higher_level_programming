#!/usr/bin/python3

def no_c(my_string):
    """To remove all chars instance of c and C from string."""
    portion = [item for item in my_string if item != 'c' and item != 'C']
    return ("".join(portion))
