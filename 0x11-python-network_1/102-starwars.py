#!/usr/bin/python3
'''Takes in a string and sends a search request to SWAPI'''
from requests import get
from sys import argv


def print_entry(r):
    '''Prints character and title'''
    for entry in r.get('results'):
        print(entry.get('name'))
        for film in entry.get('films'):
            print("\t{}".format(get(film).json().get('title')))


if __name__ == "__main__":
    r = get('https://swapi.co/api/people', params={'search': argv[1]}).json()
    print("Number of results: {}".format(r.get('count')))
    print_entry(r)
    while r.get('next'):
        r = get(r.get('next')).json()
        print_entry(r)
