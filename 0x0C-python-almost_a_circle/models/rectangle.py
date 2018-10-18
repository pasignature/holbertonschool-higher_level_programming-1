#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base


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

        for row in range(self.y):
            print()
        for row in range(self.height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        """STR Output"""

        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates Attributes"""

        if args and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                self.__setattr__(attrs[i], arg)
        else:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def to_dictionary(self):
        """Returns the dictionary repr"""

        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
