#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""

class Square:
    """ 
    class Square

    Args:
        size: size fo a side of a square
    """
    def __init__(self, size):
        """
        Initializes square

        Attribues:
            size: size of a side of a square
        """
        self.__size = size
