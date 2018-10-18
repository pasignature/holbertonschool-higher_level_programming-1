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

        if id is not None and type(id) is int and id > 0:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string repr"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
