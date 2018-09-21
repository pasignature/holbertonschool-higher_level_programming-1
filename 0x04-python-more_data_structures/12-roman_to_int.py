#!/usr/bin/python3
def roman_to_int(roman_string):
    r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    total, prev = 0, 0
    for c in roman_string:
        total += r_n[c] - 2 * prev if r_n[c] > prev else r_n[c]
        prev = r_n[c]
    return total
