#!/usr/bin/python3
"""define square class"""


class Square:
    """Represent square"""

    def __init__(self, size=0):
        """initialize the square
        args:
        size(int): the size of the square(default = 0)
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
