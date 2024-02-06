#!/usr/bin/python3

"""defines object represented by a JSON dtring"""


import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string:

    Args:
        my_str: The json string to decerialize

    Returns: object represented by JSON string
    """
    return json.loads(my_str)
