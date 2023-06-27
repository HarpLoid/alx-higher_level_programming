#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size
"""


class Square:
    """
    class Square

    Args:
        size(int): size of a side of a square

    Methods:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attribues:
            __size: size of a side of a square,
            0 if none
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the current square area

        Return:
            area
        """
        return self.__size ** 2
