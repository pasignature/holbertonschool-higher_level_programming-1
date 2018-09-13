#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if not count:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d}: arguments:".format(count))
        for n,i in enumerate(argv[1:]):
            print("{:d}: {:s}".format(n + 1, i))
