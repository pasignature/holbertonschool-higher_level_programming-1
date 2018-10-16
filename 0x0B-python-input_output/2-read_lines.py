#!/usr/bin/python3
"""Read N Lines Module"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines from a text file and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end='')
        else:
            for line in f:
                if nb_lines:
                    print(line, end='')
                else:
                    break
                nb_lines -= 1
