#!/usr/bin/python3
"""
Module - 2-rectangle
Defines a class rectangle
"""


class Rectangle:
    """
    class Rectangle

    Args:
        width: shorter side of the rectangle
        height: longer side of the rectangle

    Methods:
        __init__(self, width, height)
        width(self)
        height(self)
        width(self, value)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle

        Attributes:
            __width: shorter side of the rectangle
            __height: longer side of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter
        returns the __width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        Sets the __width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter
        returns the __height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        Sets the __height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)
