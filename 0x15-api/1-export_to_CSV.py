#!/usr/bin/python3
"""Export to CSV"""
import requests
import sys
import csv

if __name__ == "__main__":
    # get url by id:
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(sys.argv[1]))

    # covert get to json file
    List_user = users.json()
    List_todo = todo.json()

    filename = sys.argv[1] + '.csv'

    # create a csv file using with
    with open(filename, mode='w') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        # insert each item to csv file
        for item in List_todo:
            csv_writer.writerow([item['userId'], List_user['username'],
                                 item['completed'], item['title']])
