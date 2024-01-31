#!/usr/bin/python3
"""Defines a name-printing fucntion"""


def say_my_name(first_name, last_name=""):
    """
    print a  name

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.

    Raises:
        TypeError: If either of first_name or last_name are not strings

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice

        >>> say_my_name("42", "Smith")
        Error: first_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
