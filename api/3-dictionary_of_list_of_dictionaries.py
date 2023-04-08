#!/usr/bin/python3
"""Read all users and tasks"""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_api_url = "{}/users".format(base_url)
    response = requests.get(users_api_url)
    if response.status_code != 200:
        sys.exit()
    users = response.json()
    dict_users = {}
    for user in users:
        id = user["id"]
        dict_users[id] = []
        tasks_api_url = "{}/users/{}/todos".format(base_url, id)
        tasks_response = requests.get(tasks_api_url)

        tasks = tasks_response.json()

        for task in tasks:
            dict_task = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            dict_users[id].append(dict_task)
    filename = "todo_all_employees.json"
    # Serializing json
    json_object = json.dumps(dict_users)
    # Writing to sample.json
    with open(filename, "w") as outfile:
        outfile.write(json_object)
