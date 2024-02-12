#!/usr/bin/python3
""" Defines unittests foe base.py
unittest classes:
     TestBase_instantiation
     TestBase_to_json_string
     TestBase_save_to_file
     TestBase_from_json_string
     TestBase_create
     TestBase_load_from_file
     TestBase_save_to_file_csv
     TestBase_load_from_file_csv

"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """unit test for the Base class"""
    def test_id_generation(self):
        """Test id generation when id is not provided """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_provided(self):
        """Test id assignement when id is provided"""
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_id_increment(self):
        """test when id incremented for multiple instance"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_invalid_id(self):
        """Test behaviour when invalid id is provided """
        with self.assertRaises(TypeError):
            Base("invalid_id")

    def test_negative_id(self):
        """test negative id is provided """
        with self.assertRaises(ValueError) as context:
            Base(-5)
        self.assertEqual(str(context.exception),
                         "Id must be a non_negative integer")

    def test_zero_id(self):
        """Tets beaviour when id is zero """
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_large_id(self):
        """Test behaviour when id is large """
        base = Base(99999999999999999)
        self.assertEqual(base.id, 99999999999999999)

    def test_same_id(self):
        """Test behaviour when the same id is asserted """
        base1 = Base(10)
        base2 = Base(10)
        self.assertEqual(base1.id, base2.id)

    def test_no_arg(self):
        """Test when no argument is provided"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        """Test instantation of three objects and check if
        their IDs are consecutive """
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None_id(self):
        """Test instantation with None as the ID"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def unique_id(self):
        """Test instantiation with uniques ID"""
        assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """Test if the number of instances increments correctly """
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_id_public(self):
        """Test if the ID attribute is publically accessible"""
        base = Base(12)
        base.id = 15
        self.assertEqual(15, base.id)

    def test_nb_instances_private(self):
        """Test if the __nb_instances attribute is private"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb__instances)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        """Test loading the first rectangle from a CSV file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        """Test loading the second rectangle from a CSV file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        """Test if all loaded objects are instances of Rectangle."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_csv_first_square(self):
        """Test loading the first square from a CSV file."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        """Test loading the second square from a CSV file."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        """Test if all loaded objects are instances of Square."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_csv_no_file(self):
        """Test loading from an empty CSV file."""
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        """Test loading from CSV file with more than one argument."""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(cls):
        """Delete any created files after each test."""
        for file_name in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass

    def test_save_to_file_one_rectangle(self):
        """Test saving one rectangle to a JSON file."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        """Test saving two rectangles to a JSON file."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        """Test saving one square to a JSON file."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        """Test saving two squares to a JSON file."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        """Test saving objects to a JSON file with Base class name."""
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        """Test overwriting existing JSON file."""
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        """Test saving None to a JSON file."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        """Test saving an empty list to a JSON file."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        """Test calling save_to_file method with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """Test calling save_to_file method with more than one argument."""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        """Test if the output of from_json_string method is a list."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        """Test converting a JSON string with one rectangle to a list."""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """Test converting a JSON string with two rectangles to a list."""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """Test converting a JSON string with one square to a list."""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """Test converting a JSON string with two squares to a list."""
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        """Test converting None JSON string to an empty list."""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test converting an empty JSON string to an empty list."""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test calling from_json_string method with no arguments."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """Test calling from_json_string method with more than 1 argument."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        """Test creating a rectangle object using create method with
        original parameters."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        """Test creating a new rectangle object using create method."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        """Test if the newly created rectangle object is not
        the same instance as the original one."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        """Test if the newly created rectangle object is
        equal to the original one."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        """Test creating a square object using create
        method with original parameters."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        """Test creating a new square object using create method."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        """Test if the newly created square object is not the same
        instance as the original one."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """Test if the newly created square object is equal
        to the original one."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        """Test loading the first rectangle object from file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        """Test loading the second rectangle object from file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        """Test if all loaded objects from file are of type Rectangle."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_first_square(self):
        """Test loading the first square object from file."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        """Test loading the second square object from file."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        """Test if all loaded objects from file are of type Square."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_no_file(self):
        """Test loading from file when the file does not exist."""
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """Test loading from file with more than one argument."""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files after all tests are run."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        """Test saving one rectangle object to CSV file."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        """Test saving two rectangle objects to CSV file."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            content = f.read()
            self.assertTrue("5,10,7,2,8" in content and "3,2,4,1,2" in content)

    def test_save_to_file_csv_one_square(self):
        """Test saving one square object to CSV file."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        """Test saving two square objects to CSV file."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            content = f.read()
            self.assertTrue("8,10,7,2" in content and "3,8,1,2" in content)

    def test_save_to_file__csv_cls_name(self):
        """Test saving objects to CSV file with Base class name."""
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        """Test overwriting existing CSV file."""
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        """Test saving None object to CSV file."""
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        """Test saving empty list to CSV file."""
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        """Test saving with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        """Test saving with more than one argument."""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files after all tests are run."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        """Test loading first rectangle from CSV file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        """Test loading second rectangle from CSV file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        """Test types of objects loaded from CSV file (Rectangle)."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        """Test loading first square from CSV file."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        """Test loading second square from CSV file."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        """Test types of objects loaded from CSV file (Square)."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        """Test loading from non-existing CSV file."""
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        """Test loading from CSV file with more than one argument."""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
