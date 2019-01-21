#!/usr/bin/python3
'''Sends a request and displays value of X-Request-Id'''
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.info()['X-Request-Id'])
