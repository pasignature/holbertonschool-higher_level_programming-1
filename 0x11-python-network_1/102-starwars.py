#!/usr/bin/python3
'''Takes in a string and sends a search request to SWAPI'''
from requests import post, get
from sys import argv


def print_titles(films):
    '''display titles wth tabulation'''
    for film in films:
        print("\t{}".format(get(film).json().get('title')))


if __name__ == "__main__":
    r = post('https://swapi.co/api/people', params={'search': argv[1]}).json()
    print("Number of results: {}".format(r.get('count')))
    while (1):
        for entry in r.get('results'):
            print(entry.get('name'))
            print_titles(entry.get('films'))
        if r.get('next'):
            r = get(r.get('next')).json()
        else:
            break
