#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from command line arguments
    user_id = sys.argv[1]

    # Define the API endpoint URL
    url = "https://jsonplaceholder.typicode.com/"

    # Get the user details using the API endpoint and the user ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Get the to-do list of the user using the API endpoint and the user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write the user to-do list information to a JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        # Write the information as a dictionary, with the key as the user ID
        # and the value as a list of dictionaries, each containing information
        # about a to-do task
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
