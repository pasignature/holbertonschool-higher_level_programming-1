#!/usr/bin/python3
"""Full Rectangle Module"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """inits the class"""

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area and returns the value"""

        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string to be printed"""

        return '[{}] {}/{}'.format(self.__class__.__name__,
                                   self.__width, self.__height)
