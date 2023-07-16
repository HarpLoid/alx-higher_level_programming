#!/usr/bin/python3
"""
Module - base
 Base class
 """
import json


class Base():
    """ Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file
        """
        obj_list = []
        if list_objs:
            for i in list_objs:
                obj_list.append(cls.to_dictionary(i))
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf8') as f:
            f.write(cls.to_json_string(obj_list))
