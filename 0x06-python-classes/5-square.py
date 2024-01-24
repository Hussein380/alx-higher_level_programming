#!/usr/bin/python3
class Square:
    """
    This class defines square.

    Attributes:
        __size(int): Private instance attribute representing the size
        of the square
    """

    def __init__(self, size=0):
        """
            Initializaes a new instances of the square

        Args:
            size (int): optional size of the square .Defaults to 0
         """

        self.size = size

    @property
    def size(self):
        """
        GETTER METHOD FOR THE SIZE ATTRIBUTE

         Return:
                Int: The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method for the size attribute

        Args:
            value (int): the size to set

        Raises:
            TyoeError: if the size is not an intager
            ValueError: if the size is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        claculates the area of the square

        Returns:
            int: the area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        print the square pattern using the '#' character

        if the size ), prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
