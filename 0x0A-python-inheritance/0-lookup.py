#!/usr/bin/python3
"""Defines an attributes and methods of an object lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    my_list = dir(obj)
    return my_list
