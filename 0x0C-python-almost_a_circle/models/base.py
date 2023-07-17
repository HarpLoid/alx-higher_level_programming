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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the
        JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(file, 'r') as f:
                instances = cls.from_json_string(f.read())
            for i, d in enumerate(instances):
                instance_list.append(cls.create(**instances[i]))
        except Exception:
            pass
        return instance_list
