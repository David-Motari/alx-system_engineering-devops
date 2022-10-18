#!/usr/bin/python3
"""
2-export_to_json
Exports data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empId = argv[1]
    user = requests.get(url + "users/{}".format(empId)).json()
    todos = requests.get(url + "todos").json()

    userInfo = {}
    todoList = []

    for todo in todos:
        if todo.get('userId') == int(empId):
            todoDict = {"task": todo.get('title'),
                        "completed": todo.get('completed'),
                        "username": user.get('username')}
            todoList.append(todoDict)
    userInfo[empId] = todoList

    filename = empId + ".json"
    with open(filename, mode="w") as f:
        json.dump(userInfo, f)
