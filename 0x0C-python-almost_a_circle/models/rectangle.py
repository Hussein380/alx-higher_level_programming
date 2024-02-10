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
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        self.__height = value

    @property
    def x(self):
        """Getter for the x attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x attribute"""
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attribute"""
        self.__y = value
