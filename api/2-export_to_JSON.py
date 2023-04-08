#!/usr/bin/python3
"""Read user and users tasks"""

import json
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
    dict_user = {
        id: []
    }

    for task in tasks:
        dict_task = {"task": task["title"], "completed": task["completed"],
                     "username": user["username"]}
        dict_user[id].append(dict_task)

    filename = "{}.json".format(id)
    # Serializing json
    json_object = json.dumps(dict_user)
    # Writing to sample.json
    with open(filename, "w") as outfile:
        outfile.write(json_object)
