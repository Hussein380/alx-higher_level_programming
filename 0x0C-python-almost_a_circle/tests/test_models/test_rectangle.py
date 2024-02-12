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

    """def test_bool_width(self):
        Test if TypeError is raised when boolean is passsed as width
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)"""

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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        """Test if ValueError is raised when zero is passed as width """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
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
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        """Test if TyepeError is raised when string is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "innvalid", 2)

    def test_float_x(self):
        """Test if TyepeError is raised when float is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        """Test if TyepeError is raised when complex is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(2))

    def test_dict_x(self):
        """Test if TyepeError is raised when dict is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    """def test_bool_x(self):
        Test if TyepeError is raised when boolean is passed as x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)"""

    def test_list_x(self):
        """Test if TyepeError is raised when list is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        """Test if TyepeError is raised when set is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        """Test if TyepeError is raised when tuple is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        """Test if TyepeError is raised when frozenset is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        """Test if TyepeError is raised when range is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        """Test if TyepeError is raised when bytesarray is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        """Test if TyepeError is raised when memoryview is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcdefg'))

    def test_inf_x(self):
        """Test if TyepeError is raised when float('inf') is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_Nan_x(self):
        """Test if TyepeError is raised when Nan is passed as x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_Negative_x(self):
        """Test if TyepeError is raised when Negative is passed as x """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
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
        """Test if TypeError is raised when a bytearray object is passed y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        """Test if TypeError is raised when a memoryview object passed y."""
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
        """Test if ValueError is raised when a negative value is passed y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittest for testing Rectangle order of attributes initialization"""

    def test_width_before_height(self):
        """Test if TypeError is raised when width is initialized
        with an invalid before height"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        """Test if TypeError is raised when width is initialized
        with an invalid before x-coordinate"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        """Test if TypeError is raised when width is initialized
        with an invalid before y-coordinate"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        """Test if TypeError is raised when height is initialized
        with an invalid before x-coordinate"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height" "invalid x")

    def test_height_before_y(self):
        """Test if TypeError is raised when height is initialized
        with an invalid before y-coordinate"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid x")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_Area(unittest.TestCase):
    """Unit tests for the area method of the Rectangle clss """

    def test_are_small(self):
        """Test if area is correctly calculated for a small rectangle"""
        r = Rectangle(10, 2, 0, 0)
        self.assertEqual(20, r.area())

    def test_are_large(self):
        """Test if area is correctly calculated for large rectangle"""
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        expected_area = 999999999999998999000000000000001
        self.assertEqual(expected_area, r.area())

    def test_are_changed_attributes(self):
        """Test if area is correctly calculated after modifying attributes"""
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_are_one_arg(self):
        """Test if area is correctly calculated for a small rectangle"""
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on rect.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        """Test __str__ method by printing width and height."""
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        """Test __str__ method by specifying width, height,and x-coordinate."""
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        """Test __str__ method by specifying width, height, x-coordinate,
        and y-coordinate."""
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        """Test __str__ method by specifying width, height, x-coordinate,
        y-coordinate, and id."""
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        """Test __str__ method after modifying attributes."""
        r = Rectangle(7, 7, 0, 0, 4)
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] (4) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        """Test __str__ method with invalid argument."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display_width_height(self):
        """Test display method by specifying width and height."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        """Test display method by specifying width, height,x-coordinate."""
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("###\n###\n", capture.getvalue())

    def test_display_width_height_y(self):
        """Test display method by specifying width, height, y-coordinate."""
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        """Test display method by specifying width, height, x-coordinate, and
        y-coordinate."""
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n##\n##\n##\n##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """Test display method with invalid argument."""
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittest for testing update kwargs method of the Rectangle class"""

    def test_update_kwargs_one(self):
        """Test updating only the id attribute"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        """Test updating only the width and  id attribute"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        """Test updating only the width, height, id attribute"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        """Test updating all attribute"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        """Test updating all,attribute in different order"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        """Test updating id attribute with None"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        """Test updating id, height and y attributes with None"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        """Test updatingattributes twice"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=2, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/2", str(r))

    def test_update_kwargs_invalid_width_type(self):
        """Test updating with attribute invalid type """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """Test updating width attribute with zero """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        """Test updating width attribute with negative value """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """Test updating height attribute invalid type """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """Test updating heigth attribute with zero """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        """Test updating height attribute with negative value """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_invalid_x_type(self):
        """Test updating x attribute with invalid type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """Test updating x attribute with negative value"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """Test updating y attribute with invalid type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """Test updating x attribute with negative value"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


if __name__ == "__main__":
    unittest.main()
