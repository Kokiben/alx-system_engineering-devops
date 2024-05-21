#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys


def fetch_data(ud):
    # Fetch user information
    u_rp = requests.get(f"https://jsonplaceholder.typicode.com/users/{ud}")
    user_data = u_rp.json()

    # Fetch tasks information
    p = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={ud}")
    todos_data = p.json()

    return user_data, todos_data


def write_to_json(ud, username, todos):
    tasks = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username
        }
        for todo in todos
    ]
    data = {str(ud): tasks}

    filename = f"{ud}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main(ud):
    user_data, todos_data = fetch_data(ud)
    username = user_data['username']
    write_to_json(ud, username, todos_data)
    print(f"Data for user {ud} has been written to {ud}.json")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    ud = sys.argv[1]
    main(ud)
