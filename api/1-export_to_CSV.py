#!/usr/bin/python3
"""Read user and users tasks
Python script to export data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    users_api_url = "{}/users/{}".format(base_url, id)
    response = requests.get(users_api_url)
    if response.status_code != 200:
        sys.exit()
    user = response.json()
    tasks_api_url = "{}/users/{}/todos".format(base_url, id)
    tasks_response = requests.get(tasks_api_url)

    tasks = tasks_response.json()
    filename = "{}.csv".format(id)
    with open(filename, 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=',')
        for task in tasks:
            row = (str(user["id"]), user["username"],
                   str(task["completed"]), task["title"])
            my_writer.writerow(row)
