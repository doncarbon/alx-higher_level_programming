#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        notelist = list(a_dictionary.keys())
        note = 0
        leader = ""
        for i in notelist:
            if a_dictionary[i] > note:
                note = a_dictionary[i]
                leader = i
        return leader
