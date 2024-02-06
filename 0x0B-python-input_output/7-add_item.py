#!/usr/bin/python3
"""Defines a script that add all arguments to a Python list and save them to a file."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    try:
        jsonlist = load_from_json_file("add_item.json")
    except FileNotFoundError:
        jsonlist = []

    for arg in sys.argv[1:]:
        jsonlist.append(arg)
    save_to_json_file(jsonlist, "add_item.json")
