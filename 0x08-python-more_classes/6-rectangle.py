#!/usr/bin/python3
"""class #7 for rectangle project"""


class Rectangle:
    """rectangle object"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.area() == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        if self.area() == 0:
            return 0
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        if self.number_of_instances > 0:
            type(self).number_of_instances -= 1
