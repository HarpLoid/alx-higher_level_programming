#!/usr/bin/python3
"""
Module - 4-print_square
Prints a square with the '#'
character
"""


def print_square(size):
    """
    Prints a square using '#' character
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        pass
    else:
        print('\n'.join(["#" * size for rows
                            in range(size)]))
