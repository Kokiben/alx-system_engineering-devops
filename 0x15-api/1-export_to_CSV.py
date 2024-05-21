#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
import sys


def fetch_data(ud):
    # Fetch user information
    u_rps = requests.get(f"https://jsonplaceholder.typicode.com/users/{ud}")
    user_data = u_rps.json()

    # Fetch tasks information
    p = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={ud}")
    todos_data = p.json()

    return user_data, todos_data


def write_to_csv(ud, username, todos):
    filename = f"{ud}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for todo in todos:
            writer.writerow([ud, username, todo['completed'], todo['title']])


def main(ud):
    user_data, todos_data = fetch_data(ud)
    username = user_data['username']
    write_to_csv(ud, username, todos_data)
    print(f"Data for user {ud} has been written to {ud}.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    ud = sys.argv[1]
    main(ud)
