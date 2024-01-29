#!/usr/bin/python3
"""This moduule introduces Rectangle class """


class Rectangle:
    """
    class to represent retangle:

    Attributes:
        - width (int) : the width of the rectangle
        - height (int): The height of the rectangle

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes the rectangle object

        Args:
            width (int): The width of rectangle(default 0)
            height (int): The height of rectangle(default 0)
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Return a string representation of the rectangle, where each row
        is composed of the print_symbol repeated width times and
        the number of rows is qual to the heigth of rectangle

        Returns:
            -str: the string representation of the rectangle
            if width or height is equal to 0, an empty string
            is returned
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n"
                * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle

        The returned string can be used to recreate a new
        instance of the react using the eval fucntion

        Returns:
            A string representation of the form "Rectangle(width, height)"
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        destructor method for the Rectangle class

        Prints a farewell message when an instance of Rectangle is deleted
        The messasge is: "Bye rectangle..."
        Additionaly, it decrements the number_of_instances class attribute.

        Return:
            None
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @ staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method to determine the rectangle with bigger or
        equal area

        Args:
            rect_1 (Rectangle): The first rectangle to compare
            rect_2(Rectangle_): The second rectangle to compare

        Returns:
            Rectangle: The rectangle with bigger or equal area

        raises:
            TypeError: If either rect_1 or rect_2 is not an instance
            of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
