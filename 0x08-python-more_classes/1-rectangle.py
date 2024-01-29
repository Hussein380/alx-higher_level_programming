#!/usr/bin/python3
class Rectangle:
    """Class to represent rectangle"""

    def __init__(self, width=0, height=0):
        """
        - Initialize the Rectangle object


        Args:
            - width (int): the width of te rectangle (default is 0).
            - height (int): The height of the rectangle (default is 0).
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of rectangle.

        Args:
            -value (int): The new width value

        Raises:
            -TypeError: if width is not an integer.
            -ValueError: if the width is less than 0.
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
            -int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle

        Args:
            value (int): The new height value

        Raises:
            -typeError: if the height is not an int
            -ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
