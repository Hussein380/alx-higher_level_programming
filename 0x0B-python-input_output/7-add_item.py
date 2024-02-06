#!/usr/bin/python3
"""Add all arguments to a python list and save them to a file"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")

    except FileNotFoundError:
        items = []

    """Add new items from command_line arguments to the list"""
    items.extend(sys.argv[1:])

    """save the update list to the file """
    save_to_json_file(items "add_item.json")
