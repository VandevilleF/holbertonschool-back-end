#!/usr/bin/python3
"""Returns inform about his/her (employee ID) TODO list progress
and export data in the json format"""

from requests import get
import json


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':

    # get todo list
    todo = get(f"{url}/todos")
    todo_data = todo.json()

    all_user_dict = {}
    # get users info
    users = get(f"{url}/users/").json()
    for user in users:
        user_id = user["id"]

        user_dict = []
        for task in todo_data:
            if task["userId"] == user_id:
                # save info in dictonnary
                task_info = {"username": user["username"],
                             "task": task["title"],
                             "completed": task["completed"]}
                # save info inside list
                user_dict.append(task_info)

        # use the ID of the user for store all task data for this user
        all_user_dict[user_id] = user_dict

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(all_user_dict, file)
