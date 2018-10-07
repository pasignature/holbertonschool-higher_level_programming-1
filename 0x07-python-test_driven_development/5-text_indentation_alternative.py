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
    text = '\n'.join(t.strip(' ') for t in text.split('\n'))
    for c in ".?:":
        text = "{}\n\n".format(c).join(t.lstrip(' ') for t in text.split(c))
    print(text, end='')
