#!/usr/bin/python3
class Square:
    """Basic square class #5"""

    def __init__(self, size=0):
        """Initialize the square"""
        self.size = size

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculates the area"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square using # symbol"""
        row = ''.join('#' for c in range(self.size))
        print('\n'.join(row for r in range(self.size)))
