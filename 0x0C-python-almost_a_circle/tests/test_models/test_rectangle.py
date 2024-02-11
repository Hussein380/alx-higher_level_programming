#!/usr/bin/python3
"""Defines unittest for models/rectangle.py
unittest classes:
    TestRectangle_insitantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_order_of_initialization
    TestRectangle_area
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_to_dictionary

"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


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


class TestRectangleWidth(unittest.TestCase):
    """Unittest for testing Initialization of Rectangle width attribute. """

    def test_None_width(self):
        """Test if TypeError is Raised if NONe is passed as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """Test if TypeError is raised if when a string passed as a width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        """Test if the TypeError is raised if float is passed as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        """Test TypeError is raised when a complex number  passed as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        """Test if TypeError is raised when dictionary is passed as width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        """Test if TypeError is raised when boolean is passsed as width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        """Test if TypeError is raised when a list is passed as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        """Test if TypeError is raised when a set is passes as width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        """Test if TypeError is raised when a tuple is passes a s width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        """Test if TYpeError is raised if frozen set is passed as width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 2)

    def test_range_width(self):
        """Test if TypeError is raised  when range of object passeas width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        """Test if TypeError is raised when a byte object passed as width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        """Test if TypeError is raised when a memoryview obj is passed"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcdefg'), 2)

    def test_inf_width(self):
        """Test if TypeError is raised when infinity is passed"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        """test  if TypeError is raised if NaN is passed as width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        """test if TypeError is raised when negative value is passed"""
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        """Test if ValueError is raised when zero is passed as width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(0, 2)

class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_None_height(self):
        """Test if TypeError is raised if None is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """Test if TypeError is raised if string is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        """Test if TypeError is raised if float is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        """Test if TypeError is raised if `complex is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        """Test if TypeError is raised if dictionary is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        """Test if TypeError is raised if list is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        """Test if TypeError is raised if set is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        """Test if TypeError is raised if tuple is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        """Test if TypeError is raised if frozenset is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        """Test if TypeError is raised if range is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        """Test if TypeError is raised if bytes is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        """Test if TypeError is raised if bytearray is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        """Test if TypeError is raised if memoryview object passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        """Test if TypeError is raised if float(inf) is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        """Test if TypeError is raised if NaN is passd as width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        """Test if TypeError is raised if negative is passd as width"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        """Test if TypeError is raised if zero is passd as width"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittest for testing initialization of Rectangle x attribute """


    def test_None_x(self):
        """Test if TyepeError is raised when None is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        """Test if TyepeError is raised when string is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, "innvalid", 2)
                
    def test_float_x(self):
        """Test if TyepeError is raised when float is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        """Test if TyepeError is raised when complex is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, complex(2))

    def test_dict_x(self):
        """Test if TyepeError is raised when dict is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        """Test if TyepeError is raised when boolean is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        """Test if TyepeError is raised when list is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        """Test if TyepeError is raised when set is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        """Test if TyepeError is raised when tuple is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        """Test if TyepeError is raised when frozenset is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        """Test if TyepeError is raised when range is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        """Test if TyepeError is raised when bytesarray is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        """Test if TyepeError is raised when memoryview is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, memoryview(b'abcdefg'))

    def test_inf_x(self):
        """Test if TyepeError is raised when float('inf') is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_Nan_x(self):
        """Test if TyepeError is raised when Nan is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_Negative_x(self):
        """Test if TyepeError is raised when Negative is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        """Test if TypeError is raised when None is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        """Test if TypeError is raised when a string is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        """Test if TypeError is raised when a float number is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        """Test if TypeError is raised when a complex number is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        """Test if TypeError is raised when a dictionary is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        """Test if TypeError is raised when a list is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        """Test if TypeError is raised when a set is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        """Test if TypeError is raised when a tuple is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        """Test if TypeError is raised when a frozenset is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        """Test if TypeError is raised when a range object is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        """Test if TypeError is raised when a bytes object is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        """Test if TypeError is raised when a bytearray object is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        """Test if TypeError is raised when a memoryview object is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        """Test if TypeError is raised when float('inf') is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        """Test if TypeError is raised when float('nan') is passed as y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        """Test if ValueError is raised when a negative value is passed as y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)








if __name__ == "__main__":
    unittest.main()
