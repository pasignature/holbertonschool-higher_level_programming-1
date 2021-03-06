#!/usr/bin/python3
'''Requests from URL and returns body response'''
from requests import get
from requests.exceptions import HTTPError
from sys import argv


if __name__ == "__main__":
    r = get(argv[1])
    try:
        r.raise_for_status()
    except:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.content.decode('utf-8'))
