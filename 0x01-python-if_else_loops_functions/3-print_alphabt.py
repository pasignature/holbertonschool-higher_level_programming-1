#!/usr/bin/python3
for c in range(97, 123):
    if c is not 101 or c is not 113:
        print("{:s}".format(chr(c)), end='')
