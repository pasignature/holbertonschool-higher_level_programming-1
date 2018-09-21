#!/usr/bin/python3
def best_score(a_dictionary):
    name, max = None, None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if not max or v > max:
                name, max = k, v
    return name
