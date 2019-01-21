#!/usr/bin/python3
'''Fetches https://intranet.hbtn.io/status'''
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as response:
        info = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(info)))
        print("\t- content: {}".format(info))
        print("\t- utf8 content: {}".format(info.decode('utf-8')))
