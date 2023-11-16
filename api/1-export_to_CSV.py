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
        EMPLOYEE_NAME = (user_data[0]["name"])

    """ Fetching todo list based on ID """
    response_todos = requests.get(todos_url, {"userId": argv[1]})
    if response_todos.status_code == 200:
        todo_data = json.loads(response_todos.text)

    """ Initializing counters """
    tasks = 0
    completed_tasks = 0
    list_of_tasks = []

    """ Count completed tasks & create a list of their titles """
    for item in todo_data:
        if item["completed"]:
            completed_tasks += 1
            list_of_tasks.append(item["title"])
        tasks += 1

    """ Generate & print to output_format """
    output_format = "Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, completed_tasks, tasks
    )

    print(output_format)

    """ Printing titles of completed tasks with proper indentation """
    for item in list_of_tasks:
        print("\t {}".format(item))

    """ Exporting data to CSV """
    csv_file_name = "{}.csv".format(EMPLOYEE_ID)
    with open(csv_file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        """ Writing CSV header """
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        """ Writing task details """
        for task_title in list_of_tasks:
            csv_writer.writerow(
                [EMPLOYEE_ID, EMPLOYEE_NAME, "Completed", task_title])
