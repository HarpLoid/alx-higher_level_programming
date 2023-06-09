#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private attribute size
public method area, getter and setter properties
for size.
prints the square using '#'
"""


class Square:
    """
    class Square

    Args:
        size(int): size of a side of a square

    Methods:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attribues:
            __size: size of a side of a square,
            0 if none
        """
        self.size = size

    @property
    def size(self):
        """
        Getter

        Retrives the __size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Sets the __size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area

        Return:
            area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the '#' character
        """
        print('\n'.join(["#" * self.__size for rows
              in range(self.__size)]))
