#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """request num of subs"""
    header = {"User-Agent": "ymcastellar"}
    req = requests.get('https://reddit.com/r/' + subreddit
                       + '/hot.json?limit=10', headers=header)

    top = req.json().get('data', {}).get('children', None)

    if top:
        for c_title in top:
            print(c_title.get("data").get("title"))
    else:
        print(None)
