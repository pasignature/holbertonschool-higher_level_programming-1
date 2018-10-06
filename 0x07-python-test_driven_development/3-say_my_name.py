#!/usr/bin/python3
"""Task 2 - say my name
This is our function to be tested
"""


def say_my_name(first_name, last_name=''):
    """Prints the full name in a specific format

    Args:
        first_name (string): first parameter
        last_name (string): default empty

    Returns:
        Returns nothing

    Raises:
        TypeError: first and last name must be a string
    """
    te1 = "first_name must be a string"
    te2 = "last_name must be a string"
    if type(first_name) is not str:
        raise TypeError(te1)
    if type(last_name) is not str:
        raise TypeError(te2)
    print("My name is {} {}".format(first_name, last_name))
