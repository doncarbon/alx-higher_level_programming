#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = 0
    weight = 0

    for tupl in my_list:
        num += tupl[0] * tupl[1]
        weight += tupl[1]

    return num / weight
