#!/usr/bin/python3
'''Takes in a string and sends a search request to SWAPI'''
from requests import post, get
from sys import argv


def print_titles(films):
    '''display titles wth tabulation'''
    for film in films:
        print("\t{}".format(get(film).json()['title']))


if __name__ == "__main__":
    r = post('https://swapi.co/api/people', params={'search': argv[1]}).json()
    print("Number of results: {}".format(r['count']))
    while (r['count']):
        for entry in r['results']:
            print(entry['name'])
            print_titles(entry['films'])
        if r['next']:
            r = get(r['next']).json()
        else:
            break
