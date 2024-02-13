#!/usr/bin/python3
""" Defines unittests foe base.py
unittest classes:
     TestBase_instantiation

"""
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """unit test for the Base class"""
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


if __name__ == "__main__":
    unittest.main()
