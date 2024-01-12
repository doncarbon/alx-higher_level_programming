#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, values in a_dictionary.items():
        if value == a_dictionary[values]:
            del a_dictionary[values]
    return a_dictionary
