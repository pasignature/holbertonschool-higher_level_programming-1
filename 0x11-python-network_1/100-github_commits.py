#!/usr/bin/python3
'''List the ten most recent commits for a github repo'''
from sys import argv
from requests import Session, Request, get


if __name__ == "__main__":
    u = 'https://api.github.com/repos/' + argv[1] + '/' + argv[2] + '/commits'
    r = get(u)
    try:
        out = r.json()
    except:
        print("Not a valid JSON")
    else:
        for entry in out[:10]:
            sha = entry['sha']
            name = entry['commit']['author']['name']
            print("{}: {}".format(sha, name))
