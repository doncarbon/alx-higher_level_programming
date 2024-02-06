#!/usr/bin/python3
"""Defines writing an Object using JSON to a file."""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (str): the object to convert and write.
        filename (str): path to the filename.
    """
    import json
    with open(filename, 'w', encoding="UTF8") as f:
        cnv = json.dumps(my_obj)
        chars = f.write(cnv)
