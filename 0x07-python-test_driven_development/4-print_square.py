#!/usr/bin/python3

"""
print a square with the character #
"""


def print_square(size):
    """
    prints a square where size is the length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
