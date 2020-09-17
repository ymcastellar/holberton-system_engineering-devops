#!/usr/bin/python3
"""querie the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """request num of subs"""
    header = {"User-Agent": "ymcastellar"}
    req = requests.get('https://reddit.com/r/' + subreddit + '/about.json',
                       headers=header, allow_redirects=True)

    if req.status_code != 200:
        return 0

    return req.json().get('data', {}).get('subscribers', 0)
