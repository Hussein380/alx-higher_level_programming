#!/usr/bin/python3
"""This moduule introduces Rectangle class """


class Rectangle:
    """
    class to represent retangle:

    Attributes:
        - width (int) : the width of the rectangle
        - height (int): The height of the rectangle

    """

    def __init__(self, width=0, height=0):
        """
        initializes the rectangle object

        Args:
            width (int): The width of rectangle(default 0)
            height (int): The height of rectangle(default 0)
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Retrn:
            int: The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle

        Args:
            - Value (int): The new width value

        Raises:
            typeError: width must be an integer
            ValueError:  width must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
        -int: The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the rectangle.

        Args:
            - value (int): The new height value

        Raises:
        - TypeError: if the height is not an int
        - Value: if the height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate the return the area of the rectangle

        Return:
            Int: the area of the rectangle

        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle

        Returns:
            -int: The perimeter of the rectangle

        """

        return 2 * (self.__width + self.__height) if self.__width and \
            self.__height else 0
