#!/usr/bin/python3
'''Takes in a string and sends a search request to SWAPI'''
from requests import post, get
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
        while (out['next']):
            out = get(out['next']).json()
            for entry in out['results']:
                print(entry['name'])
