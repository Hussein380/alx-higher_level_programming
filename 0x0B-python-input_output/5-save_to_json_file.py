#!/usr/bin/python3

"""defines fucntion that writes objet to text file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation

    Args:
        my_obj: The object to serialize into JSON and write to the file
        filename (str): The name of the file to write to
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
