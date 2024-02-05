#!/usr/bin/python3
""" Defines an inherited list from class mylist"""


class MyList(list):
    """Implement sorted printing for the builtin list class"""

    def print_sorted(self):
        """prints a list in sorted ascending order"""
        print(sorted(self))
