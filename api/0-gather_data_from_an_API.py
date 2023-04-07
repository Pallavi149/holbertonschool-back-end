#!/usr/bin/python3
import requests
import sys


id = int(sys.argv[1])
users_api_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
response = requests.get(users_api_url)
if response.status_code != 200:
    sys.exit()
user = response.json()
tasks_api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
   id)
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
