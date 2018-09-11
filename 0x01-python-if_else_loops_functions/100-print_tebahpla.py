#!/usr/bin/python3
for c in range(122, 96, -1):
    offset = 0
    if c % 2:
        offset = 32
    print("{:s}".format(chr(c - offset)), end='')
