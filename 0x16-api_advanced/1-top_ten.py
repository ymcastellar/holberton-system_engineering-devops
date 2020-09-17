#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """request num of subs"""
    URL = 'http://reddit.com/r/{}/hot.json'
    headers = {"User-Agent": "ymcastellar"}
    size_q = {'limit': 10}

    responsable = requests.get(URL.format(
        subreddit), params=size_q, headers=headers)

    top = req.json().get('data', {}).get('children', None)

    if top:
        for c_title in top:
            print(c_title.get("data").get("title"))
    else:
        print("None")
