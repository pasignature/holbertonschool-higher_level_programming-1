#!/usr/bin/python3
'''finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    '''finds a peak in a list of unsorted integers'''
    if list_of_integers:
        a = 0
        b = len(list_of_integers) - 1
        if a == b:
            return list_of_integers[a]
        if list_of_integers[a] > list_of_integers[1]:
            return list_of_integers[a]
        if list_of_integers[b] > list_of_integers[b - 1]:
            return list_of_integers[b]
        mid = (b - a) // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid + 1:])
        return list_of_integers[mid]
    return None
