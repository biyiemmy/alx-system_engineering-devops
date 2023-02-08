#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    # base URL for the API endpoint
    url = "https://jsonplaceholder.typicode.com/"

    # retrieve a list of all users from the API
    users = requests.get(url + "users").json()

    # create a JSON file to store the data for all employees
    with open("todo_all_employees.json", "w") as jsonfile:
        # write the data to the file
        json.dump({
            # iterate through the users
            u.get("id"): [{
                # add task information for each user
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
