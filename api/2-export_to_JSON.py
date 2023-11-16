#!/usr/bin/python3
""" Task 0, Gathering data from an API """
import json
from requests import get
from sys import argv

""" API endpoints """
url = "https://jsonplaceholder.typicode.com/users/"
todos_url = "https://jsonplaceholder.typicode.com/todos/"


def get_response():
    """ Fetching user data based on ID """
    response_user = get(url, {"id": argv[1]})
    if response_user.status_code == 200:
        user_data = json.loads(response_user.text)

    """ Fetching todo list based on ID """
    response_todos = get(todos_url, {"userId": argv[1]})
    if response_todos.status_code == 200:
        todo_data_list = json.loads(response_todos.text)

    new_list = []

    """ Count completed tasks & create a list of their titles """
    for item in todo_data_list:
        username = user_data[0]["username"]
        completed_todo = item["completed"]
        title_of_todo = item["title"]
        new_dict = {"task": title_of_todo, "completed": completed_todo,
                    "username": username}
        new_list.append(new_dict)
    dict_for_user = {str(argv[1]): new_list}

    return dict_for_user


def writing_json(dict_to_write):
    """ Write the input dict to json """
    json_file_name = "{}.json".format(argv[1])
    with open(json_file_name, "w") as json_file:
        json.dump(dict_to_write, json_file)


if __name__ == "__main__":
    response_dict = get_response()
    writing_json(response_dict)
