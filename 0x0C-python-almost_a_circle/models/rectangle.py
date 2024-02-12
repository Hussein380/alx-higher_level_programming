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
        if value <= 0:
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

    def display(self):
        """print the Rectangle using # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Return a string representation of the Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle

        Args:
            *args (int): New attribute values
                -1st argument represent id attribute
                -2nd argument should be the width attribute
                -3rd argument should be the height attribute
                -4th argument should be the x attribute
                -5th argument should be the y attribute

        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    """if the first argument is None reset the rectangle"""
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            """if keyword argument are provided"""
            for k, v in kwargs.items():
                if k == "id":
                    """if id key is None , reset the rectangle"""
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary representation of Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y


                 }
