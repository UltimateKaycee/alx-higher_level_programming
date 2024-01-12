#!/usr/bin/python3

def best_score(a_dictionary):
    """Function to return a key with the largest int value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    grab = list(a_dictionary.keys())[0]
    largest = a_dictionary[grab]
    for r, o in a_dictionary.items():
        if o > largest:
            largest = o
            grab = r
    return (grab)
