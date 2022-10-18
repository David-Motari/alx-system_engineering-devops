#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries
Exports data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    allTasks = {}
    todoList = []
    for user in users:
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                todoDict = {"username": user.get('username'),
                            "task": todo.get('title'),
                            "completed": todo.get('completed')}
                todoList.append(todoDict)
        allTasks[user.get('id')] = todoList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(allTasks, f)
