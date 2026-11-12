#!/usr/bin/python3
"""Export all tasks belonging to one employee as JSON."""

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

    records = [{"task": task["title"], "completed": task["completed"],
                "username": employee["username"]} for task in tasks]
    with open("{}.json".format(employee_id), "w", encoding="utf-8") as output:
        json.dump({str(employee_id): records}, output)
