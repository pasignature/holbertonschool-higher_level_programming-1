#!/usr/bin/python3
'''Takes my github credentials and uses gh api to display my id'''
from requests.auth import HTTPBasicAuth
from requests import get
from sys import argv


if __name__ == "__main__":
    auth = argv[1]
    if len(argv) > 2:
        auth = (argv[1], argv[2])
    r = get('https://api.github.com/user', auth=auth)
    try:
        out = r.json()
    except:
        print("Not a valid JSON")
    else:
        print(out['id'])
