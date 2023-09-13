#!/usr/bin/python3

"""Pascals triangle"""


def pascal_triangle(n):
    """returns list of lists"""
    if n <= 0:
        return []
    matrix = [[1]]
    while len(matrix) != n:
        m = matrix[-1]
        tmp = [1]
        for i in range(len(m) - 1):
            tmp.append(m[i] + m[i + 1])
        tmp.append(1)
        matrix.append(tmp)
    return matrix
