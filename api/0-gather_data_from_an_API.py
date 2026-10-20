#!/usr/bin/python3
"""Return TODO list progress for a given employee ID using a REST API."""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    EMPLOYEE_NAME = requests.get(f"{url}/users/{id}").json()["name"]
    ALL_TODOS = requests.get(f"{url}/todos").json()
    TOTAL_NUMBER_OF_TASKS = [t for t in ALL_TODOS if t["userId"] == int(id)]
    NUMBER_OF_DONE_TASKS = [
        t["title"] for t in TOTAL_NUMBER_OF_TASKS if t["completed"]
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
    for title in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(title))
