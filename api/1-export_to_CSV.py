#!/usr/bin/python3
""" Task 0, Gathering data from an API """
import csv
import json
import requests
from sys import argv

""" API endpoints """
url = "https://jsonplaceholder.typicode.com/users/"
todos_url = "https://jsonplaceholder.typicode.com/todos/"

if __name__ == "__main__":

    """ Fetching user data based on ID """
    response_user = requests.get(url, {"id": argv[1]})
    if response_user.status_code == 200:
        user_data = json.loads(response_user.text)
        EMPLOYEE_ID = user_data[0]["id"]
        EMPLOYEE_NAME = (user_data[0]["username"])

    """ Fetching todo list based on ID """
    response_todos = requests.get(todos_url, {"userId": argv[1]})
    if response_todos.status_code == 200:
        todo_data_list = json.loads(response_todos.text)

    BIG_task_list = []

    for todo_data in todo_data_list:
        completed = todo_data["completed"]
        title = todo_data["title"]
        new_list = [EMPLOYEE_ID, EMPLOYEE_NAME, completed, title]
        BIG_task_list.append(new_list)

    csv_file_name = "{}.csv".format(EMPLOYEE_ID)

    with open(csv_file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for item in BIG_task_list:
            csv_writer.writerow(item)
