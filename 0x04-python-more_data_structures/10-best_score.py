#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    name, max = None, None
    for k, v in a_dictionary.items():
        if name == None:
            name, max = k, v
        elif v > max:
            name = k
            max = v
    return name
