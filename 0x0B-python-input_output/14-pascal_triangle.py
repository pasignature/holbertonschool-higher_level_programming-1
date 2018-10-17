#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """Returns a list of list of integers repr Pascal's Triangle of n"""

    if n <= 0:
        return ans
    ans = [[1]]
    if n == 1:
        return ans
    for i in range(1, n):
        new = []
        for i in range(1, len(ans[-1])):
            new.append(ans[-1][i - 1] + ans[-1][i])
        ans.append([1] + new + [1])
    return ans
