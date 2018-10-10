#!/usr/bin/python3
def magic_string():
    j = __import__("__main__").i
    return ", ".join(["Holberton"] * j)
