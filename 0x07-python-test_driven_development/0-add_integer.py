#!/usr/bin/python3
"""Task 0 - add integer
This is our function to be tested
"""


def add_integer(a, b=98):
    """Add two integers together
    Args:
        a (int or float): First param
        b (int or float): Second param; default 98

    Returns:
        Returns the integer sum of a and b

    Raises:
        TypeError: if either a or b is neither an integer nor a float

    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
