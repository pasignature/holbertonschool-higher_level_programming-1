#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    if len(argv) == 1:
        sum = 0
    else:
        for n in range(1, len(argv)):
            sum += int(argv[n])
    print("{:d}".format(sum))
