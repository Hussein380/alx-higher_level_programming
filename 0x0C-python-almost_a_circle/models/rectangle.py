#!/usr/bin/python3
"""Module defining class the Rectangle , inheriting from Base"""


from models.base import Base


class Rectangle(Base):
    """class Representing rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The iheight of the rectangle
            x (int): The x-cordinate of the rectangle's position Default to 0
            y (int): The c-cordinate of the rectangle's position Default to 0
            id (int): The Id of the rectangle . Default to 0

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self,  value):
        """Setter for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for the x attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of the rectangle"""
        return self.width * self.height
