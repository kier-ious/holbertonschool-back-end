#!/usr/bin/python3
""" Task 0, Gathering data from an API """
import json
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com/users/"
todos_url = "https://jsonplaceholder.typicode.com/todos/"

response = requests.get(url, {"id": argv[1]})
if response.status_code == 200:
    user_data = json.loads(response.text)
    EMPLOYEE_NAME = (user_data[0]["name"])

response = requests.get(todos_url, {"userId": argv[1]})
if response.status_code == 200:
    todo_data = json.loads(response.text)

tasks = 0
completed_tasks = 0
list_of_tasks = []

for item in todo_data:
    if item["completed"]:
        completed_tasks += 1
        list_of_tasks.append(item["title"])
    tasks += 1

output_format = "Employee {} is done with tasks({}/{}):".format(
    EMPLOYEE_NAME, completed_tasks, tasks
)

print(output_format)

for item in list_of_tasks:
    print("\t {}".format(item))
