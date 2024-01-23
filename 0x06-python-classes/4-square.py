#!/usr/bin/python3
""""Defines a square"""


class Square:
    """Represent a square """

    def __init__(self, size=0):
        """initialize the new square

        Args:
            size int: the size of the new square (default =0)

        Raises:
            TypeError: if size is not intager
            ValueError: if size iss less tan 0
        """

        self.__size = size

    @property
    def size(self):
        """Retrieves Yhe size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """initialize the new square

        Args:
            size int: the size of the new square (default =0)

        Raises:
            TypeError: if size is not intager
            ValueError: if size iss less tan 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """gets the area of the square:"""

        return self.__size ** 2
