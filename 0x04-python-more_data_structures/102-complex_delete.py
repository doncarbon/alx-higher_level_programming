#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in a_dictionary:
        if value == a_dictionary[key]:
            del a_dictionary[key]
    return a_dictionary
