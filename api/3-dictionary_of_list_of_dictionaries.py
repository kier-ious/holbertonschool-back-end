#!/usr/bin/python3
""" basic request to json file """
from requests import get
from sys import argv
import json


""" API endpoints """
url = "https://jsonplaceholder.typicode.com/users/"
todos_url = "https://jsonplaceholder.typicode.com/todos/"

if __name__ == "__main__":
    all_employees_data = {}

    def get_response():
        """ Fetching user data based on ID """
        response_user = get(url)
        if response_user.status_code == 200:
            user_data = json.loads(response_user.text)
            username = user_data[0]["username"]
            userId = user_data[0]["id"]

        """ Fetching todo list based on ID """
        response_todos = get(todos_url)
        if response_todos.status_code == 200:
            todo_data_list = json.loads(response_todos.text)

            user_tasks = []

            """ Count completed tasks & create a list of their titles """
            for item in todo_data_list:
                task_title = item["title"]
                completed_status = item["completed"]
                task_data = {
                    "username": username,
                    "task": task_title,
                    "completed": completed_status}
                user_tasks.append(task_data)

            all_employees_data[str(userId)] = user_tasks

        def writing_json(dict_to_write):
            """ Write the input dict to json """
            file_name = "todo_all_employees.json"
            with open(file_name, "w") as json_file:
                json.dump(all_employees_data, json_file)

        get_response()
        writing_json(all_employees_data)
