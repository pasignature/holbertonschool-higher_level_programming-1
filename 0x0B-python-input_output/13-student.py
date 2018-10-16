#!/usr/bin/pyton3
"""Student To Disk And Reload"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dict repr of Student"""

        if attrs:
            d = {}
            for k in attrs:
                if k in self.__dict__.keys():
                    d[k] = self.__dict__[k]
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the instances"""

        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']