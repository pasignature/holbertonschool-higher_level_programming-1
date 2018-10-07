#!/usr/bin/python3
"""Task 4 - add newlines function
This is our function to be tested
"""


def text_indentation(text=''):
    """Adds 2 newlines following specific characters

    Args:
        text (str):: first parameter

    Returns:
        Returns nothing

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for c in ".?:":
        text = text.replace(c, c + "\n\n")
    print('\n'.join(t.strip() for t in  text.split('\n')), end='')
