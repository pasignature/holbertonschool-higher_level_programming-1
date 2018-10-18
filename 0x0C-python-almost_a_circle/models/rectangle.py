#!/usr/bin/python3
from models.base import Base

"""Rectangle Module"""


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Me!"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width Getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Height Getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter"""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """X Getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """X Setter"""

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Y Getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """Y Setter"""

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the Area"""

        return self.width * self.height

    def display(self):
        """Display Shape"""

        for row in range(self.height):
            print('{}'.format('#') * self.width)