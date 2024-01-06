#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for start in matrix:
        print(' '.join('{:d}'.format(starter)for starter in start))
