#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    if count == 1:
        print("0")
    elif count == 2:
        print("{:d}".format(int(argv[1])))
    else:
        print("{:d}".format(int(argv[1]) + int(argv[2])))
