#!/usr/bin/python3
"""list containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], key=None):
    """return all hot articles"""

    URL = 'http://reddit.com/r/{}/hot.json'
    headers = {"User-Agent": "ymcastellar"}

    if key:
        req = requests.get(URL.format(
            subreddit), params=key, headers=headers)
    else:
        req = requests.get(URL.format(
            subreddit), headers=headers)

    sub_json = req.json()
    sub_data = sub_json['data']
    page = sub_data['after']
    top = sub_data['children']

    if top:
        for c_title in top:
            hot_list.append(c_title.get("data").get("title"))

    if key:
        recurse(subreddit, hot_list, key)

    return hot_list
