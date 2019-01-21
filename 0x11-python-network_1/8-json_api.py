#!/usr/bin/python3
'''Takes in a letter and send a POST request'''
from requests import post
from sys import argv


if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    r = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        out = r.json()
    except:
        print("Not a valid JSON")
    else:
        if out:
            print("[{}] {}".format(out['id'], out['name']))
        else:
            print("No result")
