#!/usr/bin/python3
'''Fetches from https://intranet.hbtn.io/status'''
from requests import get


if __name__ == "__main__":
    r = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.content.decode('utf-8')))
