#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    the_list = my_list[:]
    for vent, start in enumerate(my_list):
        if start % 2 == 0:
            the_list[vent] = True
        else:
            the_list[vent] = False
    return(the_list)
