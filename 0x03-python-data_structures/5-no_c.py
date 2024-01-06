#!/usr/bin/python3
def no_c(my_string):
    temp = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            temp += ''
        else:
            temp += my_string[i]
    return temp
