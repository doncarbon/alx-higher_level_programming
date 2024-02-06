#!/usr/bin/python3
"""Defines a str to json str conversion function."""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (str): object to convert.

    Returns:
        the JSON str of my_obj.
    """
    import json
    cnv = json.dumps(my_obj)
    return cnv
