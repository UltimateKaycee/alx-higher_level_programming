#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """To replace element in a copied list
    at a position without original list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    part = [item for item in my_list]
    part[idx] = element
    return (part)
