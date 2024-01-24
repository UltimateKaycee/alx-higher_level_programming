#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function to print x elememts of a list.

        my_list (list): The list.
        x (int): num of elements to print.

        Will return num printed elements
    """
   the_return = 0
    for start in range(x):
        try:
            print("{}".format(my_list[start]), end="")
            the_return += 1
        except IndexError:
            break
    print("")
    return (the_return)
