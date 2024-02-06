#!/usr/bin/python3
"""Defines  fucntion that returns JSON"""


import json


def to_json_string(my_obj):
    """
    Returns  the Json representation of an object

    Args:
        my_obj: the object to serailize into JSON

    Returns:
        str: The JSON representation of the object
    """

    json_rep = json.dumps(my_obj)

    return json_rep
