#!/usr/bin/python3
"""
Module - 8-rectangle
class Rectangle that inherits from BaseGeometry
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
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height