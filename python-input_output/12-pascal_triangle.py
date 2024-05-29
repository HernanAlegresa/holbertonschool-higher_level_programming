#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of (n).
    """
    if n <= 0:
        return []

    triangle = []
    row = []
    last_row = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for x in range(len(last_row) - 1):
                row.append(last_row[x] + last_row[x + 1])
            row.append(1)
        triangle.append(row)
    return triangle
