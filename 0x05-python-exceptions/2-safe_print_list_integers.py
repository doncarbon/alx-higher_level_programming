#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers = 0
    s = 0
    while s < x:
        try:
            print("{:d}".format(my_list[s]), end="")
            integers += 1
            s += 1
        except IndexError:
            break
        except (ValueError, TypeError):
            s += 1
    print("")
    return integers
