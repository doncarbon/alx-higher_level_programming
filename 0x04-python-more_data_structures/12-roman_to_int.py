#!/usr/bin/python3
def roman_to_int(roman_string):
    import string
    num = []
    total = 0
    if not isinstance(roman_string, str) or roman_string == 'None':
        return 0

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    letters = list(roman_string)
    for i in range(len(letters)):
        for key, value in values.items():
            if letters[i] == key:
                num.append(values[key])

    num.reverse()
    for idx in range(len(num)):
        if idx == 0:
            total += num[idx]
        elif 0 < idx < len(num):
            if num[idx] < num[idx - 1]:
                total -= num[idx]
            else:
                total += num[idx]
    #            for idx2 in range(1, len(num)):
    #                if num[idx] > num[idx2]:
    #                   cnv += num[idx] + num[idx2]
    #                else:
    #                    cnv += num[idx] - num[idx2]
    return total
