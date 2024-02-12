#!/usr/bin/python3

"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation
    TestSquare_size
    TestSquare_x
    TestSquare_y
    TestSquare_order_of_initialization
    TestSquare_area
    TestSquare_stdout
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        """Test if Square is an instance of Base."""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """Test if Square is an instance of Square."""
        self.assertIsInstance(Square(10), Square)

    # Testing number of arguments
    def test_no_args(self):
        """Test instantiation with no arguments."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test instantiation with one argument."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """Test instantiation with two arguments."""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """Test instantiation with three arguments."""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """Test instantiation with four arguments."""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """Test instantiation with more than four arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    # Testing attribute access
    def test_size_private(self):
        """Test access to private attribute size."""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """Test size getter method."""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """Test size setter method."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """Test width getter method."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """Test height getter method."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """Test x getter method."""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """Test y getter method."""
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    # Testing invalid size types
    def test_None_size(self):
        """Test None type for size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """Test string type for size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        """Test float type for size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    # Other type checks omitted for brevity...

    # Testing negative and zero sizes
    def test_negative_size(self):
        """Test negative size value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        """Test zero size value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


# Other test classes omitted for brevity...


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        """Test output of to_dictionary method."""
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """Test if object changes with to_dictionary method."""
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """Test to_dictionary method with an argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
