#!/usr/bin/python3
"""Defins a class and inherrited a class checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance
    of a class

    Args:
        obj (any): The object to check
        a_class (type): the class to match the type of obj to

    Returns:
        if obj is an instance of inherited class - True

    """

    if isinstance(obj, a_class):
        return True
    return False
