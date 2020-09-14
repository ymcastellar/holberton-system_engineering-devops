#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    # get url by id:
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(sys.argv[1]))

    # covert get to json file
    List_user = users.json()
    List_todo = todo.json()

    dict = {}
    new_list = []

    # create a new dict with the user items
    for item in List_todo:
        task_user = {}
        task_user["task"] = item['title']
        task_user["completed"] = item['completed']
        task_user["username"] = List_user['username']
        new_list.append(task_user)

    dict[sys.argv[1]] = new_list
    # json file name
    new_file = sys.argv[1] + '.json'
    # insert items in file
    with open(new_file, mode='w') as jfile:
        json.dump(dict, jfile)
