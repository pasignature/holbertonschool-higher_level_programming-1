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
        lst = []
        for entry in out:
            sha = entry['sha']
            author = entry['commit']['author']['name']
            date = entry['commit']['author']['date']
            lst.append((sha, author, date))
    lst.sort(key=lambda x: x[2], reverse=True)
    for entry in lst[:10]:
        print("{}: {}".format(entry[0], entry[1]))
