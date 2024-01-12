#!/usr/bin/python3

def weight_average(my_list=[]):
    """Function to return weighted average of integers in tuple."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    average = 0
    the_size = 0
    for my_tuple in my_list:
        average += (my_tuple[0] * my_tuple[1])
        the_size += my_tuple[1]
    return (average / the_size)
