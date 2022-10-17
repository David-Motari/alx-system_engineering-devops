#!/usr/bin/python3
"""
0-gather_data_from_an_API
returns information about his/her TODO list progress for a given employee ID
using a REST API
"""
import requests
from sys import argv


def main():
    url = "https://jsonplaceholder.typicode.com/"
    employeeId = int(argv[1])
    rqst = requests.get('{}users/{}'.format(url, employeeId))
    employee = rqst.json()
    empName = employee.get('name')
    rqst2 = requests.get('{}todos'.format(url), params={'userId': employeeId})
    tasks = rqst2.json()
    completed = []
    for task in tasks:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        empName, len(completed), len(tasks)))
    for complete in completed:
        print("\t {}".format(complete))


if __name__ == "__main__":
    main()
