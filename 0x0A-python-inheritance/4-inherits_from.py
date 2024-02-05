#!/usr/bin/python3
""" Defines an inherited class_checking function"""


def inherits_from(obj, a_class):
    """Checks if an obj is  inherited instance of a class

    Args:
        obj(any): The obj to check
        a_class (type): The class to match the type of obj to.
    Return:
        if obj is an inherited instance of a_class - True
    otherwise - False
    """

    """if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
