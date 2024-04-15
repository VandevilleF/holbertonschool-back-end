#!/usr/bin/python3
"""Returns inform about his/her (employee ID) TODO list progress"""

from requests import get
from sys import argv
import json


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':

    # get users info with ID
    user_id = int(argv[1])
    users = get(f"{url}/users/{user_id}").json()

    # get todo list
    todo = get(f"{url}/todos")
    todo_data = todo.json()

    user_dict = []
    for task in todo_data:
        if task["userId"] == user_id:
            # save info in dictonnary
            task_info = {"task": task["title"],
                         "completed": task["completed"],
                         "username": users["username"]}
            # save info inside list
            user_dict.append(task_info)

    with open(f"{argv[1]}.json", "w", encoding="utf-8") as jsonfile:
        json.dump({users["id"]: user_dict}, jsonfile)
