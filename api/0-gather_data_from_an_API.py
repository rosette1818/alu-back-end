#!/usr/bin/python3
"""Display an employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    employee = requests.get(
        "{}/users/{}".format(base_url, employee_id)).json()
    tasks = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    completed = [task for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task.get("title")))