#!/usr/bin/python3
"""
0-gather_data_from_an_API
returns information about his/her TODO list progress for a given employee ID
using a REST API
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empId = argv[1]
    employee = requests.get(url + "/users/{}".format(empId))

    name = employee.json().get('name')

    tasks = requests.get(url + 'todos').json()
    totalTasks = 0
    completed = 0

    for task in tasks:
        if task.get('userId') == int(empId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in tasks
          if task.get('userId') == int(empId) and task.get('completed')]))
