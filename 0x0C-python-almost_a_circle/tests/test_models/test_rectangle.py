#!/usr/bin/python3
"""Defines unittest for models/rectangle.py
unittest classes:
    TestRectangle_instantiation(unittest.TestCase)

"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_instantiation(unittest.TestCase):
    """unit test for testing instantiation of the Rectangle class """

    def test_rectangle_is_base(self):
        """Tests  if the rectangle inherits from the base"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_arguments(self):
        """Test if instantiation without providing any arguments """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """test if instantiation with only one argument """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test instantiation with two arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test instantiation with three arguments"""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test instantiation with four arguments """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Test instantiation wit five arguments"""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test more than five arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_attributes(self):
        """Test if te width, height, x and y are private attributes """
        rectangle = Rectangle(5, 5, 0, 0, 1)
        with self.assertRaises(AttributeError):
            print(rectangle.__width)
        with self.assertRaises(AttributeError):
            print(rectangle.__height)
        with self.assertRaises(AttributeError):
            print(rectangle.__x)
        with self.assertRaises(AttributeError):
            print(rectangle.__y)

    def test_width_getter_setter(self):
        """Test getter and setter for height attribute """
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rectangle.height)
        rectangle.height = 10
        self.assertEqual(10, rectangle.height)

    def test_x_getter_setter(self):
        """Test getter and setter for x attribute """
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rectangle.x)
        rectangle.x = 10
        self.assertEqual(10, rectangle.x)

    def test_x_getter_setter(self):
        """Test getter and setter for x attribute """
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rectangle.y)
        rectangle.y = 10
        self.assertEqual(10, rectangle.y)


if __name__ == "__main__":
    unittest.main()
