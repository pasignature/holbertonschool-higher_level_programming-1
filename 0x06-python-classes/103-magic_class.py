#!/usr/bin/python3
class MagicClass:
    """magic class
    filler text 1
    filler text 2
    """

    def __init__(self, radius):
        """Initialize magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference"""
        return 2 * math.pi * self.__radius
