#!/usr/bin/python3
"""Defines MyInt class inherited from Int"""


class MyInt(int):
    """Inverting int operators == and !="""

    def __eq__(self, value):
        """Invert == behavior with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Invert != behavior with == behavior."""
        return self.real == value
