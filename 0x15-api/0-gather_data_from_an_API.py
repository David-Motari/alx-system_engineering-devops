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
    rqst = requests.get(url + "users/{}".format(argv[1]))
    employee = rqst.json()
    rqst2 = requests.get(url + "todos", params={"userId": argv[1]})
    tasks = rqst2.json()

    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(complete)) for complete in completed]


if __name__ == "__main__":
    main()
