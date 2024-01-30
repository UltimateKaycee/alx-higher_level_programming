#!/usr/bin/python3
"""Module for a function for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices.

    Arguments - m_a (list of lists of ints and floats): First matrix.
        m_b (list of lists of ints and floats): Second matrix.
    Gives TypeError if either m_a or m_b is not list of lists
    of ints and floats, if either m_a or m_b is empty,
    if either m_a or m_b has different row sizes and
    ValueError, if m_a and m_b can't be multiplied.
    Will return a new matrix of multiplying m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for item in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    other_b = []
    for bear in range(len(m_b[0])):
        new_row = []
        for rat in range(len(m_b)):
            new_row.append(m_b[rat][bear])
        other_b.append(new_row)

    new_matrix = []
    for rw in m_a:
        new_row = []
        for cl in other_b:
            give = 0
            for start in range(len(other_b[0])):
                give += rw[start] * cl[start]
            new_row.append(give)
        new_matrix.append(new_row)

    return new_matrix
