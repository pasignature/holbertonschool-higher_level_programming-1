#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square Class Module"""


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Me!"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size Getter"""

        return self.width

    @size.setter
    def size(self, value):
        """Size Setter"""

        self.width = value
        self.height = value

    def __str__(self):
        """STR output"""

        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)
