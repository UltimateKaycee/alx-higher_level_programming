#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """To compute square value of integers of a matrix."""
    return ([list(map(lambda rowitem: rowitem * rowitem, hor)) for hor in matrix])