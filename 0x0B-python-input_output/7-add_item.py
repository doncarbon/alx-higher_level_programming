#!/usr/bin/python3
"""Defines a script that add all arguments to a Python list and save them to a file."""
import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file


if __name__ == "__main__":
    try:
        jsonlist = load_from_json_file("add_item.json")
    except FileNotFoundError:
        jsonlist = []

    for arg in range(len(sys.argv)):
        jsonlist.append(arg)

    save_to_json_file(jsonlist, "add_item.json")
