#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    the_list = []

    for start in range(len(my_list)):
        if my_list[start] % 2 == 0:
            the_list.append(True)
        else:
            the_list.append(False)

    return (the_list)
