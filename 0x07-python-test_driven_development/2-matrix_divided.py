#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module that divides a matrix
    author: peter ekwere

"""


def matrix_divided(matrix, div):
    """
    divides every item in the matrix by div
    """
    try:
        row_sizes = len(matrix[0])
        j = 1
        new_matrix = []
        for row in matrix:
            if len(row) != row_sizes:
                raise TypeError("Each row of the matrix "
                                "must have the same size")
            for item in row:
                if not isinstance(item, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) "
                                    "of integers/floats")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        for row in matrix:
            new_row = []
            for item in row:
                number = item / div
                rounded_num = round(number, 2)
                new_row.append(rounded_num)
            new_matrix.append(new_row)

        return new_matrix
    except (TypeError, ZeroDivisionError) as e:
        return str(e)
