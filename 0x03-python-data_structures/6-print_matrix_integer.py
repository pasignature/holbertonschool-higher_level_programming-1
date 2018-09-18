#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for e in row[0:-1]:
            print("{:d}".format(e), end=' ')
        if row:
            print("{:d}".format(row[-1]), end='')
        print()
