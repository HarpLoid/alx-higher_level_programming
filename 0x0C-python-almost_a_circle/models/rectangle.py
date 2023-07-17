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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    def area(self):
        """
        calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        prints to stdout the Rectangle instance
        with character '#'
        """
        print('\n' * self.__y, end="")
        print('\n'.join([" " * self.__x +
                         "#" * self.__width
                         for rows in range(self.__height)]))

    def __str__(self):
        """
        prints the string representation of
        the class
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the class
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.__width = value
                elif key == 2:
                    self.__height = value
                elif key == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
