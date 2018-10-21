#!/usr/bin/python3
"""Base Model Module"""

import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Me!

        Args:
            id - int value greater than 0
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string repr"""

        if not isinstance(list_dictionaries, list):
            return "[]"
        if not len(list_dictionaries):
            return "[]"
        if not all([isinstance(e, dict) for e in list_dictionaries]):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string repr to a file"""

        res = [o.to_dictionary() for o in list_objs]
        with open(cls.__name__ + '.json', "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of jSON string repr"""

        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances read from a file"""

        with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
            text = f.read()
        obj_list = []
        for d in cls.from_json_string(text):
            obj_list.append(cls.create(**d))
        return obj_list
