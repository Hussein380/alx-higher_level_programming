#!/usr/bin/python3
"""Module defining the Base class """
import json
import csv
import turtle


class Base:
    """Base class for managing attributes of all classes of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes base instance with optional id

        Args:
            id (int, optional): Unique identifier. Default to None
        """

        if id is not None:
            if not isinstance(id, int):
                raise TypeError("Id must be an integer")
            elif id < 0:
                raise ValueError("Id must be a non_negative integer")

            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json serialization of a list of dicts

        Args:
            "list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json serialzation of a list of objects to a file

        Args:
            list_obj (list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return desearealization of JSON string

        Args:
            json_string(str): A JSON str representation of a list od dicts

        Returns:
            if is None or jsoon_string = "[]"
            otherwise - the python list represented by json_string
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes

        Args:
            **dictionary (dict): key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from file of json strings
        Reads from '<cls._name_>.json'.

        Returns:
            if file does not exist - an empty list
            otherwise - a list of instantiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
