#!/usr/bin/python3
"""REST API, for a given employee ID, TODO list progress"""
import requests
import sys


def get_em_todo_progress(em_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{em_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print(f"Error: Employee with ID {em_id} not found.")
        return

    employee = employee_response.json()
    em_name = employee['name']

    # Fetch employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={em_id}"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list.")
        return

    todos = todos_response.json()

    # Calculate TODO list progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task['completed']]
    nbr_tasks = len(done_tasks)

    # Print the required output
    print(f"Employee {em_name} is done with tasks({nbr_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <em_id>")
    else:
        try:
            em_id = int(sys.argv[1])
            get_em_todo_progress(em_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
