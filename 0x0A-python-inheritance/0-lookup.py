#!/usr/bin/pyhton3
"""Defines a class_checking function """

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    return (dir(obj))
