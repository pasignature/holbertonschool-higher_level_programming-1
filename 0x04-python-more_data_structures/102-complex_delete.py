#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lst = []
    for k, v in a_dictionary.items():
        if v is value:
            lst.append(k)
    for k in lst:
        del a_dictionary[k]
    return a_dictionary
