#!/usr/bin/python3
"""Returns inform about his/her (employee ID) TODO list progress
and export data in the CSV format"""

from requests import get
from sys import argv
from csv import writer, QUOTE_ALL


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':

    # get users info with ID
    user_id = int(argv[1])
    users = get(f"{url}/users/{user_id}").json()

    # get todo list
    todo = get(f"{url}/todos")
    todo_data = todo.json()

    with open(f"{argv[1]}.csv", "w", newline="") as csvfile:
        csvwriter = writer(csvfile, quoting=QUOTE_ALL)

        for task in todo_data:
            if task["userId"] == user_id:
                csvwriter.writerow([users["id"], users["username"],
                                    task["completed"], task["title"]])
