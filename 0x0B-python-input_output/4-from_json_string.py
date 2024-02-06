#!/usr/bin/python3
"""Defines a json str to str conversion function."""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): object to convert.

    Returns:
        the object represented by a JSON str.
    """
    import json
    cnv = json.loads(my_str)
    return cnv
