#!/usr/bin/python3
"""list containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], key=None):
    """return all hot articles"""

    headers = {'User-agent': 'ymcastellar'}
    if key:
        req = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json?after=' + key,
                           headers=headers)
    else:
        req = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json', headers=headers)

    if req.status_code == 404:
        return None

    sub_json = req.json()
    sub_data = sub_json['data']
    key = sub_data['after']
    sub_children = sub_data['children']

    for children in sub_children:
        children_data = children['data']
        hot_list.append(children_data['title'])

    if key:
        recurse(subreddit, hot_list, key)
    return hot_list
