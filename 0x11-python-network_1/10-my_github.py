#!/usr/bin/python3
'''Takes my github credentials and uses gh api to display my id'''
from requests import get
from sys import argv


if __name__ == "__main__":
    pw = ""
    if len(argv) > 2:
        pw = argv[2]
    r = get('https://api.github.com/user', auth=(argv[1], pw))
    try:
        out = r.json()
    except:
        print("Not a valid JSON")
    else:
        print(out.get('id'))
