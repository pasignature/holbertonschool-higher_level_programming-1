#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c is not ord('e') or c is not ord('q'):
        print("{:s}".format(chr(c)), end='')
