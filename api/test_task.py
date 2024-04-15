#!/usr/bin/python3
"""Returns inform about his/her (employee ID) TODO list progress"""

from requests import get
from sys import argv


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':

    # get users info with ID
    user_id = int(argv[1])
    users = get(f"{url}/users/{user_id}").json()

    # get todo list
    todo = get(f"{url}/todos")
    todo_data = todo.json()

    # get task for user spéficied by ID
    task_todo = []
    for task in todo_data:
        if task["userId"] == user_id:
            task_todo.append(task)
    print(task_todo)
