#!/usr/bin/python3
def remove_char_at(str, n):
    word = ''
    for c in str:
        if n:
            word += c
        n -= 1
    return (word)
