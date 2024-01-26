#!/usr/bin/python3
# doctest_0_add_integer.py
def add_integer(a, b=98):
    """Function that adds 2 integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) in [float] or type(b) in [float]:
        a = int(a)
        b = int(b)

    return a + b
