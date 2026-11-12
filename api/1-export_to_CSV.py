#!/usr/bin/python3
"""Export all tasks belonging to one employee as quoted CSV records."""

import csv
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

    with open("{}.csv".format(employee_id), "w", newline="",
              encoding="utf-8") as output:
        writer = csv.writer(output, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, employee["username"],
                             task["completed"], task["title"]])
