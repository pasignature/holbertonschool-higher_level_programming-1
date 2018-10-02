#!/usr/bin/python3
class Square:
    """Basic square class #6"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter"""
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

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position settter"""
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Calculates the area"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square using # symbol"""
        if not self.size:
            print()
        else:
            row = ''
            row += ' ' * self.position[0]
            row += ''.join('#' for c in range(self.size))
            result = ''.join('\n' for i in range(self.position[1]))
            result += '\n'.join(row for r in range(self.size))
            print(result)
