#!/usr/bin/python3
'''Takes in a string and send request to the Star Wars API'''
from requests import post
from sys import argv


if __name__ == "__main__":
    r = post('https://swapi.co/api/people', params={'search': argv[1]})
    try:
        out = r.json()
    except:
        print("Not a valid JSON")
    else:
        count = out['count']
        print("Number of results: {}".format(count))
        for entry in out['results']:
            print(entry['name'])
