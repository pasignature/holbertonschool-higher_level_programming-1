#!/usr/bin/python3
'''Sends a request to a URL and displays body'''
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
