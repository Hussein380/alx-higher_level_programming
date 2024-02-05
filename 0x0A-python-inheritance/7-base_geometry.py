#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Represent integer validator

        Args:
            name (str): the name of the parameter
            value (int): The parameter to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is < 0


        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
