#!/usr/bin/python3
"""
print square with #
"""


def print_square(size):
    """
    function that prints a square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
