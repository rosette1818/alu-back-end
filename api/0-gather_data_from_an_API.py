#!/usr/bin/python3
"""Display an employee's TODO list progress."""

import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    with urllib.request.urlopen(
            "{}/users/{}".format(base_url, employee_id)) as response:
        employee = json.load(response)
    with urllib.request.urlopen(
            "{}/todos?userId={}".format(base_url, employee_id)) as response:
        tasks = json.load(response)

    completed = [task for task in tasks if task["completed"]]
    print("Employee {} is done with tasks({}/{}):".format(
        employee["name"], len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task["title"]))
