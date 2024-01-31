#!/usr/bin/python3
"""introduces a modules that divides"""


def matrix_divided(matrix, div):

    """
    defines a fucntion that divides mall element of a matric

    Args:
        matrix: list of intagers or floats
        div: number that divides

    Raises:
        TypeError: if matrix or div  is not an integer or float
                    if each row of the matrix is not the same size
        ZeroDivisionError: if div is equal to zero

    Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]


    """

    """
    matrix must be a list of lists of integers or floats, otherwise
    raise a TypeError exception with the message matrix must be a
     matrix (list of lists) of integers/floats
    loop over the row to access the row elements
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    """
    Each row of the matrix must be of the same size, otherwise raise
    a TypeError exception with the message Each row of the matrix
    must have the same size
    """

    first_row_length = len(matrix[0])

    # compare the length of the first row with the rest
    if not all(len(row) == first_row_length for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    """
    div must be a number (integer or float), otherwise
    raise a TypeError exception with the message div must be a number
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """
    div can’t be equal to 0, otherwise raise
    a ZeroDivisionError exception with the message division by zero
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Returns a new matrix
    new_matrix = [[round(element / div, 2) for element in
                   row] for row in matrix]
    return (new_matrix)
