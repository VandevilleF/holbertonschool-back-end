#!/usr/bin/python3
"""Returns inform about his/her (employee ID) TODO list progress"""

from requests import get
from sys import argv
from csv import writer


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':

    # get users info with ID
    user_id = int(argv[1])
    users = get(f"{url}/users/{user_id}").json()
    print(users)
