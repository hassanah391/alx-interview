#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """return a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = []
    import math
    for i in range(n):
        row = [math.comb(i, k) for k in range(i + 1)]
        triangle.append(row)

    return triangle
