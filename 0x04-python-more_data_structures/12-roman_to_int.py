#!/usr/bin/python3
def roman_to_int(roman_string):
    r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return None
    for c in roman_string:
        if c not in ['I', 'V', 'X', 'L', 'C', 'D']:
            return None
    total = 0
    prev = 0
    for c in roman_string:
        total += r_n[c]
        if r_n[c] > prev:
            total -= 2 * prev
        prev = r_n[c]
    return total
