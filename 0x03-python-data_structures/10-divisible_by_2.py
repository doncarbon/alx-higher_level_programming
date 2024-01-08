#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    torf = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            torf.append(True)
        else:
            torf.append(False)
    return torf
