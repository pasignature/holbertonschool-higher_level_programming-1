#!/usr/bin/python3
"""Sqaure #1 Module"""


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

    def area(self):
        """Calculates area and returns the value"""

        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string to be printed"""

        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initializes the square"""

        super().__init__(size, size)
