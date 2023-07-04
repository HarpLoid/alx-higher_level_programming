#!/usr/bin/python3
"""
Module - 2-matrix_divided
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all the elements of matrix
    Returns a new list with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(matrix_error)

    dividend_matrix = []
    row_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_error)
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        dividend_row = []
        for _ in row:
            if not isinstance(_, (int, float)):
                raise TypeError(matrix_error)
            dividend_row.append(round(_/div, 2))
        dividend_matrix.append(dividend_row)
    return dividend_matrix
