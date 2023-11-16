#!/usr/bin/python3
""" Task 0, Gathering data from an API """
import json
import requests
from sys import argv
url = "https://jsonplaceholder.typicode.com/users/"
todos_url = "https://jsonplaceholder.typicode.com/todos/"

response = requests.get(url, {"id": argv[1]})
if response.status_code == 200:
    var = json.loads(response.text)
    EMPLOYEE_NAME = (var[0]["name"])

response = requests.get(todos_url, {"userId": 1})
if response.status_code == 200:
    var = json.loads(response.text)
    # NUMBER_OF_DONE_TASKS = (var[0]["completed"])
    print(var)

tasks = 0
completed_tasks = 0
list_of_tasks = [0]

for item in var:
    if item["completed"]:
        completed_tasks += 1
        list_of_tasks.append(item)
    tasks += 1
print(completed_tasks)
