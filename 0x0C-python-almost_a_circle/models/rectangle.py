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

        self.__width = value

    @property
    def height(self):
        """Height Getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter"""

        self.__height = value

    @property
    def x(self):
        """X Getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """X Setter"""

        self.__x = value

    @property
    def y(self):
        """Y Getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """Y Setter"""

        self.__y = value
