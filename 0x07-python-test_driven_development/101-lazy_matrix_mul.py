#!/usr/bin/python3

"""We define function for a matrix multiplication NumPy module."""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """Output product two matrices.

    Arguments are m_a (list of lists of integers/floats) - first matrix
    and m_b (list of lists of integers/floats) - second matrix.
    """

    return (npy.matmul(m_a, m_b))
