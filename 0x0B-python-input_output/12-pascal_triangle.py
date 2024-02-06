#!/usr/bin/python3
"""For a function that returns lists for Pascal's Triangle."""


def pascal_triangle(n):
    """Function for returning a list of lists that represent Pascal's Trianglen.

    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        beam = triangles[-1]
        touch = [1]
        for c in range(len(beam) - 1):
            touch.append(beam[c] + beam[c + 1])
        touch.append(1)
        triangles.append(touch)
    return triangles
