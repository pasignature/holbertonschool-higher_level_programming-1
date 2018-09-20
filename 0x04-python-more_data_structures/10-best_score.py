#!/usr/bin/python3
def best_score(a_dictionary):
    name, max = None, None
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if name is None:
                name, max = k, v
            elif v > max:
                name = k
                max = v
    return name
