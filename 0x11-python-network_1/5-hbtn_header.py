#!/usr/bin/python3
'''Requests from URL and returns X-R from https://intranet.hbtn.io/status'''
from requests import get
from sys import argv


if __name__ == "__main__":
    r =  get(argv[1])
    print(r.headers['X-Request-Id'])
