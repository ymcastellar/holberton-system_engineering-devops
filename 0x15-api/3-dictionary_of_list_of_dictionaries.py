#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    # get url by id:
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    List_user = users.json()

    dict = {}

    for U_name in List_user:
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(U_name['id']))
        List_todo = todo.json()

        new_list = []

        # create a new dict with the user items
        for item in List_todo:
            task_user = {}
            task_user["task"] = item['title']
            task_user["completed"] = item['completed']
            task_user["username"] = U_name['username']
            new_list.append(task_user)

        dict[U_name['id']] = new_list

    # json file name
    new_file = 'todo_all_employees.json'
    # insert items in file
    with open(new_file, mode='w') as jfile:
        json.dump(dict, jfile)
