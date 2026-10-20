#!/usr/bin/python3
"""Return TODO list progress for a given employee ID using a REST API."""
import requests
import sys

try:
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{url}/users/{id}", timeout=10).json()
    todos = requests.get(f"{url}/todos", timeout=10).json()

    EMPLOYEE_NAME = user["name"]
    TOTAL_NUMBER_OF_TASKS = [t for t in todos if t["userId"] == int(id)]
    NUMBER_OF_DONE_TASKS = [
        t["title"] for t in TOTAL_NUMBER_OF_TASKS if t["completed"]
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
    for title in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(title))
except Exception as e:
    print("ERROR:", repr(e))
