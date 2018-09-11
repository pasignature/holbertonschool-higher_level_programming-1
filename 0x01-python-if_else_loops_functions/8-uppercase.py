#!/usr/bin/python3
def uppercase(str):
    for c in str:
        offset = 0
        if ord(c) > 96 and ord(c) < 123:
            offset = -32
        print("{:s}".format(chr(ord(c) + offset)), end='')
    else:
        print()
