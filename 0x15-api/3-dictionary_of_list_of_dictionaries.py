#!/usr/bin/python3
""" Python script to export data in the JSON format"""
import json
import requests

# Fetch the data from the API
u_rsp = requests.get("https://jsonplaceholder.typicode.com/users")
tds_rsp = requests.get("https://jsonplaceholder.typicode.com/todos")

# Ensure the responses are successful
if u_rsp.status_code == 200 and tds_rsp.status_code == 200:
    us = u_rsp.json()
    tds = tds_rsp.json()

    # Prepare the data structure for the output
    all_tsk = {}

    # Create a dictionary mapping user IDs to usernames
    u_dict = {user['id']: user['username'] for user in us}

    # Populate the all_tasks dictionary
    for todo in tds:
        u_id = todo['userId']
        if u_id not in all_tsk:
            all_tsk[u_id] = []
        tsk_ifo = {
            "username": u_dict[u_id],
            "task": todo['title'],
            "completed": todo['completed']
        }
        all_tsk[u_id].append(tsk_ifo)

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tsk, json_file, indent=4)
else:
    print("Failed to fetch data from the API")
