#!/usr/bin/python3
"""Export every employee's tasks as a dictionary of lists of dictionaries."""

import json
import urllib.request


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    with urllib.request.urlopen(base_url + "/users") as response:
        employees = json.load(response)
    with urllib.request.urlopen(base_url + "/todos") as response:
        tasks = json.load(response)

    records = {str(employee["id"]): [] for employee in employees}
    usernames = {employee["id"]: employee["username"]
                 for employee in employees}
    for task in tasks:
        records[str(task["userId"])].append({
            "username": usernames[task["userId"]],
            "task": task["title"],
            "completed": task["completed"]
        })

    with open("todo_all_employees.json", "w", encoding="utf-8") as output:
        json.dump(records, output)
