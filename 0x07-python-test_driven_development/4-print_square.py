#!/usr/bin/python3
"""Task 3 - prints a square
This is our function to be tested
"""


def print_square(size):
    """Prints a square made with the char #

    Args:
        size (int):: first parameter

    Returns:
        Returns nothing

    Raises:
        TypeError: size must be an integer
        ValueError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for r in range(size):
        print("#" * size)
