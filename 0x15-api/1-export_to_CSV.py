#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

# Import the csv module for working with CSV files
# Import the requests module for making HTTP requests
# Import the sys module for accessing command line arguments
import csv
import requests
import sys

# Check if the script is being run as a standalone program
if __name__ == "__main__":
    # Get the employee ID from the first command line argument
    user_id = sys.argv[1]
    # Define the base URL of the REST API
    url = "https://jsonplaceholder.typicode.com/"
    # Get the user information for the employee with the given ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    # Extract the username from the user information
    username = user.get("username")
    # Get the to-do list information for the employee with the given ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Open a new CSV file for writing with the name <user_id>.csv
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write a row to the CSV file for each task in the to-do list
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")])
         for t in todos]
