#!/usr/bin/python3
"""Define a square"""


class Square:
    """initialize the the new square"""

    def __init__(self, size=0):
        """initialize the new square
        Args:
        size(int): The size of the newsquare
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns and clalculates the area"""
        return self.__size ** 2
