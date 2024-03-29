#!/usr/bin/python3
"""Add all arguments to a python list and save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")

    except FileNotFoundError:
        items = []

    """Add new items from command_line arguments to the list"""
    items.extend(sys.argv[1:])

    """save the update list to the file """
    save_to_json_file(items, "add_item.json")
