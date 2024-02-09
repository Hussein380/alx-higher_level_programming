#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module defining the Base class """


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
