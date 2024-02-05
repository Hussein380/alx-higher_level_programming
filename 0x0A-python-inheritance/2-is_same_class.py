#!/usr/bin/python3
"""Defines a class checking function"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class
class.

    Args:
        obj (any): The object check
        a_class (type): The match to match the type of obj to.
    Returns:
        if obj is exactly an instance of a_class - true
        otherwise - False
    """

    if type(obj) == a_class:
        return True
    return False
