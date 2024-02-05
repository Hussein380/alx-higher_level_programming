#!/usr/bin/python3
"""Defines a Rectangle subclass square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square """

    def __init__(self, size):
        """initialize a new square

        Args:
            size (int): Te size of the new square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
