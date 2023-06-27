#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private attribute size
"""


class Square:
    """
    class Square

    Args:
        size: size fo a side of a square
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attribues:
            size: size of a side of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
