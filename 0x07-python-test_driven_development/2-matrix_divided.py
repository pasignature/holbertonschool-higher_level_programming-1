#!/usr/bin/python3
"""Task 1 - matrix divide
This is our function to be tested
"""


def matrix_divided(matrix, div):
    """Divides a list of integers or floats

    Args:
        matrix (list): a list of integers or floats
        div (int or div): second parameter

    Returns:
        Returns a new matrix

    Raises:
        TypeError: if the mattric or div is of the incorrect type
        ZeroDivisionError: if div is 0

    """
    te1 = "matrix must be a matrix (list of lists) of integers/floats"
    te2 = "Each row of the matrix must have the same size"
    te3 = "div must be a number"
    zde = "division by zero"
    if type(matrix) is not list or not len(matrix):
        raise TypeError(te1)
    rowsizecheck = 0
    for row in matrix:
        if type(row) is not list or not len(row):
            raise TypeError(te1)
        if rowsizecheck:
            if len(row) != rowsize:
                raise TypeError(te2)
        else:
            rowsizecheck = 1
            rowsize = len(row)
        for e in row:
            if type(e) not in [int, float]:
                raise TypeError(te1)
    if type(div) not in [int, float]:
        raise TypeError(te3)
    if div == 0:
        raise ZeroDivisionError(zde)
    new = []
    for row in matrix:
        newrow = list(map(lambda x: round(x / div, 2), [e for e in row]))
        new.append(newrow.copy())
    return new
