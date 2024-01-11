#!/usr/bin/python3
def roman_to_int(roman_string):
    import string
    num = []
    cnv = 0
    if not isinstance(roman_string, str) or roman_string == 'None':
        return 0

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    letters = list(roman_string)
    for i in range(len(letters)):
        for key, value in values.items():
            if letters[i] == key:
                num.append(values[key])
    if len(num) == 1:
        cnv = num[0]
    for idx in range(len(num)):
        for idx2 in range(1, len(num)):
            if num[idx] > num[idx2]:
                cnv += num[idx] + num[idx2]
    return cnv
