#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Function to print first x and only integers elements of list.

    Arguments:
        my_list (list): The list.
        x (int): num of elements of.

    Will return num of printed elements.
    """
    the_return = 0
    for run in range(0, x):
        try:
            print("{:d}".format(my_list[run]), end="")
            the_return += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (the_return)
