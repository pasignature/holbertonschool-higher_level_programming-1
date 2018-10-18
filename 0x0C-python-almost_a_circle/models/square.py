#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square Class Module"""


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Me!"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """STR output"""

        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)
