#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Function to divide lists element 2 list.

    Arguments:
        my_list_1 (list): list one.
        my_list_2 (list): list two.
        list_length (int): num of elements.

    Will return new list with all the divisions.
    """
    the_list = []
    for run in range(0, list_length):
        try:
            the_div = my_list_1[run] / my_list_2[run]
        except TypeError:
            print("wrong type")
            the_div = 0
        except ZeroDivisionError:
            print("division by 0")
            the_div = 0
        except IndexError:
            print("out of range")
            the_div = 0
        finally:
            the_list.append(the_div)
    return (the_list)
