#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    """
    Main function of the script.
    Retrieves employee information and to-do list information using the
    REST API, and prints the to-do list progress for the employee.
    """

    # Base URL for the API endpoints
    url = "https://jsonplaceholder.typicode.com/"
    # Endpoint to get employee info
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    # Endpoint to get todo list for the employee
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    # Print employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
