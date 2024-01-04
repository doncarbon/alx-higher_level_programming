#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

summ = 0
if len(argv) == 1:
    print("0")
elif len(argv) > 1:
    for i in range(1, len(argv)):
        summ += int(argv[i])
    print("{}".format(summ))
