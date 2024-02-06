#!/usr/bin/python3
"""Defines creating an Object from a JSON file."""


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): path to the filename.
    """
    import json
    with open(filename, 'r', encoding="UTF8") as f:
        content = json.loads(f.read())

    return content
