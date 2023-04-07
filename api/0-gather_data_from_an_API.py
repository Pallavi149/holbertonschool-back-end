#!/usr/bin/python3
"""Read user and users tasks"""

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
    total = 0
    done = 0
    for task in tasks:
        total = total + 1
        if task["completed"]:
            done = done + 1

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], done, total))

    for task in tasks:
        if task["completed"]:
            print("\t {}".format(task["title"]))
