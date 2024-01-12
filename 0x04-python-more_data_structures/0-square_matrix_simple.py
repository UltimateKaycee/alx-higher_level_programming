#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """To compute square value of integers of a matrix."""
    return ([list(map(
                    lambda item: item * item, hor)) for hor in matrix])
