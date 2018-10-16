#!/usr/bin/python3
"""Read N Lines Module"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines from a text file and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            nb_lines and print(line, end='')
            nb_lines -= 1
