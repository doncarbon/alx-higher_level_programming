#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        rvalues = 0, "None"
    else:
        rvalues = len(sentence), sentence[0]
    return rvalues
