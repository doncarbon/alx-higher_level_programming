#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    s = 0
    while s < x:
        try:
            print(f"{my_list[s]}", end="")
            s += 1
        except IndexError:
            break
    print("")
    return s
