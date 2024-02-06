#!/usr/bin/python3
"""Defines a JSON file reading function"""
import json


def load_from_json_file(filename):
    """Creates a python object from Json FILE"""
    with open(filename) as f:
        data = json.load(f)
    return data
