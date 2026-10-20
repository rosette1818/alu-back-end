#!/usr/bin/python3

import requests
import sys

id = sys.argv[1]

url = "https://jsonplaceholder.typicode.com"

EMPLOYEE_NAME = requests.get(f"{url}/users/{id}").json()["name"]
ALL_TODOS = requests.get(f"{url}/todos").json()
TOTAL_NUMBER_OF_TASKS = [t for t in ALL_TODOS if t["userId"] == int(id)]
NUMBER_OF_DONE_TASKS = [t["title"] for t in TOTAL_NUMBER_OF_TASKS if t["completed"]]

print(f"Employee {EMPLOYEE_NAME} is done with tasks({len(NUMBER_OF_DONE_TASKS)}/{len(TOTAL_NUMBER_OF_TASKS)}):")
for title in NUMBER_OF_DONE_TASKS:
    print(f"\t {title}")