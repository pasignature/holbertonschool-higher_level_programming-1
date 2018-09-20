#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    num = sum(map(lambda x: x[0] * x[1], my_list))
    den = sum(map(lambda x: x[1], my_list))
    return num / den
