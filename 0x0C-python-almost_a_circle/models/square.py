#!/usr/bin/python3
"""
Module - square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ [Square] (<id>) <x>/<y> - <size> """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the class
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.__x = value
                else:
                    self.__y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return  dictionary
