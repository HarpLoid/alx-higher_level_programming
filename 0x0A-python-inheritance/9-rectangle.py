#!/usr/bin/python3
"""
Module - 9-rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    
    class Rectangle
    
    Attributes:
        width
        height
        
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """
        validate and initialize width and height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """extends parent's empty method and returns area"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)