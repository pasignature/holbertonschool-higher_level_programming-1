#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for e in my_list:
        if not e % 2:
            res.append(True)
        else:
            res.append(False)
    return res
