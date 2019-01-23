#!/usr/bin/python3
'''Sends a search request to Twitter API'''
from requests import post, get
from sys import argv
from base64 import b64encode


if __name__ == "__main__":
    tok = 'https://api.twitter.com/oauth2/token'
    ser = 'https://api.twitter.com/1.1/search/tweets.json'
    key = argv[1].encode('utf-8')
    sec = argv[2].encode('utf-8')
    b64bt = b64encode(key + ':'.encode('utf-8') + sec)
    b64bt = 'Basic '.encode('utf-8') + b64bt
    hdrs = {'Authorization': b64bt,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    params = {'grant_type': 'client_credentials'}
    at = post(tok, headers=hdrs, params=params).json().get('access_token')
    hdrs = {'Authorization': 'Bearer ' + at}
    params = {'q': argv[3],
              'count': 5,
              'tweet_mode': 'extended'}
    r = get(ser, headers=hdrs, params=params).json()
    for entry in r.get('statuses'):
        tid = entry.get('id')
        text = entry.get('full_text')
        if entry.get('retweeted_status'):
            text = entry.get('retweeted_status').get('full_text')
        name = entry.get('user').get('name')
        print("[{}] {} by {}".format(tid, text, name))
