#!/usr/bin/python3
"""
1-export_to_CSV
Exports data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empId = argv[1]
    user = requests.get(url + "users/{}".format(empId)).json()
    name = user.get("username")
    todos = requests.get(url + "todos").json()

    filename = empId + ".csv"
    with open(filename, mode="w") as f:
        wrtr = csv.writer(
            f, delimiter=",", quotechar='"',
            quoting=csv.QUOTE_ALL, lineterminator="\n")
        for todo in todos:
            if todo.get("userId") == int(empId):
                wrtr.writerow(
                    [empId, name, str(todo.get("completed")),
                        todo.get("title")])
