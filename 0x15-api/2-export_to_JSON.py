#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(emp_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump({emp_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
