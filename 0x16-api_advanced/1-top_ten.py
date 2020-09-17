#!/usr/bin/python3
"""prints the titles of the first 10 hot posts
    listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """request num of subs"""
    header = {"User-Agent": "ymcastellar"}
    req = requests.get('https://reddit.com/r/' + subreddit
                       + '/hot.json?sort=hot&limit=10',
                       headers=header, allow_redirects=True)

    if req.status_code != 200:
        print(None)
        return

    top = req.json().get('data', {}).get('children', None)
    for i in top:
        c_data = i.get('data')
        c_title = c_data.get('title')
        print(c_title)
