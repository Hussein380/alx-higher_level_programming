#!/usr/bin/python3

"""Defines a class studemt"""


class Student:
    """epresent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student

        Args:
            first_name (str): The name of te student
            last_name (str): The last name of the student
            age (int): The age of te student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student
        If attrs is a list of strings, represents only those attributes
        inlude in the list

        Args:
            attr (list): (optional) The attributes to represent

        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr
                                           in attrs):

            return {key: value for key, value in self.__dict__.items() if key
                    in attrs}
        return self.__dict__

    def reload_from_json(self, json):

        """Replace all attributes of te student

        Args:
            json (dict): The key/Value pairs to replace attributes with.

        """
        for k, v in json.items():
            setattr(self, k, v)
