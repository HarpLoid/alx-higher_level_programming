#!/usr/bin/python3
"""
Module - rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    inherit from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter
        returns the __width attribute
        """
        return self.__width

    @property
    def height(self):
        """
        getter
        returns the __height attribute
        """
        return self.__height

    @property
    def x(self):
        """
        getter
        returns the __x attribute
        """
        return self.__x

    @property
    def y(self):
        """
        getter
        returns the __y attribute
        """
        return self.__y

    @width.setter
    def width(self, value):
        """ sets the value of __width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the value of __height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ sets the value of __x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ sets the value of __y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
