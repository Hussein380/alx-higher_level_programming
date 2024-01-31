#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test case for the max_integer fucntion
    """

    def test_regular_list(self):
        """Test with regular list of positive numbers
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """
        Test with an unordered list of positive numbers
        """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """
        Test with a list of negative numbers
        """
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_empty_list(self):
        """
        Test with an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """
        Test with a single element list
        """
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_numbers(self):
        """
        Test with a list of dulicate numbers
        """
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_numbers(self):
        """
        Test with a list of mixed positive and negative numbers
        """
        self.assertEqual(max_integer([-5, -8, -1, -3]), -1)

    def test_zero_in_list(self):
        """
        Test with zero in the list
        """
        self.assertEqual(max_integer([0, -5, 3, 2]), 3)

    def test_large_numbers(self):
        """
        Test with large numbers in the list
        """
        self.assertEqual(max_integer([1000000, 999999, 10000000]), 10000000)


if __name__ == '__main__':
    unittest.main()
