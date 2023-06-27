#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private attribute size
public method area, getter and setter properties
for size.
prints the square using '#' also add the position
of the square
"""


class Square:
    """
    class Square

    Args:
        size(int): size of a side of a square

    Methods:
        __init__(self, size, position)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Attribues:
            size(int): size of a side of a square,
            0 if none
            position(int): tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter

        Retrives __position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        sets the __position attribute
        """
        if not isinstance(value, tuple) or len(value) != 2\
                or not isinstance(value[0], int)\
                or not isinstance(value[1], int) or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of \
                        2 positive integers")
        else:
            self.__position = value

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
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            print('\n'.join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
