#!/usr/bin/python3
"""list containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], key=None):
    """return all hot articles"""

    headers = {"User-Agent": "ymcastellar"}

    if key:
        req = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json?after=' + page,
                           headers=headers)
    else:
        req = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json', headers=headers)

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
