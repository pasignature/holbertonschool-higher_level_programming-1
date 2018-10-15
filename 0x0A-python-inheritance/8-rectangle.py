#!/usr/bin/python3
"""Rectangle Module"""


class BaseGeometry:
    """Basic class definition"""

    def area(self):
        """Empty method only used to raise Exception message"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value"""

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')

class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """inits the class"""

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
