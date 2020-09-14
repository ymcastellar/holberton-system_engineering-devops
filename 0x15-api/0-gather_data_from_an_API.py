#!/usr/bin/python3
"""Gather data from an API"""
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

    task_cont = 0
    task_done = 0
    titles_done = []

    # run into key to take values
    for task in List_todo:
        if task['completed'] is True:
            task_done += 1
            titles_done.append(task['title'])
        task_cont += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(List_user['name'], task_done, task_cont))

    for list_titles in titles_done:
        print('\t {}'.format(list_titles))
