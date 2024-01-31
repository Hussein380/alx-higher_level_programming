#!/usr/bin/python3
"""
This module introduces square
"""


def print_square(size):
    """
    Prints a square made of '#' characters.

    Args:
        `size (int): The size length of the square.

    Raises:
        -TypeError: If size is not an integer
        - ValueError: If size is less than 0.

    Example:
        >>> print_sqaure(4)
        ####
        ####
        ####
        ####

        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########

        >>> print_square(0)

        >>> print_square(1)
        #

        >>> try:
        ...     print_square(-1)
        ... except Exception as e:

        ...     print(e)
        size must be >= 0

        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
