#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keyslist = list(a_dictionary.keys())
    for values in keyslist:
        if value == a_dictionary[values]:
            del a_dictionary[values]
        return a_dictionary
