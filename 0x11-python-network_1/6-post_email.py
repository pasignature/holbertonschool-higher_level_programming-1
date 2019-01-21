#!/usr/bin/python3
'''Sends POST request'''
from requests import post
from sys import argv


if __name__ == "__main__":
    r = post(argv[1], data={'email': argv[2]})
    print(r.text)
