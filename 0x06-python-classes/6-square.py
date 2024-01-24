#!/usr/bin/python3
"""Define square class"""


class Square:
    """square class with private instance attribute: size and  position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.
        Args:
            size (int) : The size of the square )(defaultt is 0)
            position (tuple): The position of the square (default (0,)))
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size

        Returns:
            int: the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """

        setter method for position.

        Args:
            Value (int): The size to set

        Raises:
            TypeError: if size is not an intager
            ValueError: if size is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """

        Getter method for position.

        Raises:
            Tuple: the position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        setter method for position

        Args:
        value (tuple): The position to set

        Raises:
            TypeError: If position is not a tuple of 2 positove int
        """
        if(
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates and return the area of the square

        Return:
            int: Te area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        prints the square using '#' character.

        If size is 0, print empty lne
        utilize position to add spaces printing square
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("" * self.__position[0], end="")
                print("#" * self.__size)
