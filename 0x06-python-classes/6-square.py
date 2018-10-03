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
        errmsg = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple:
            raise TypeError(errmsg)
        elif len(value) != 2:
            raise TypeError(errmsg)
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError(errmsg)
        elif value[0] < 0 or value[1] < 0:
            raise TypeError(errmsg)
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
            for i in range(self.position[1]):
                print()
            row = ' ' * self.position[0]
            row += ''.join('#' for c in range(self.size))
            print('\n'.join(row for r in range(self.size)))
