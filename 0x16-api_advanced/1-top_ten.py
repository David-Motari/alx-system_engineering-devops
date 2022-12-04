#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    top ten title posts
    """
    i = 0
    headers = {"User-agent": "David-Motari"}
    req = requests.get(
        "http://reddit.com/r/{}/hot.json".format(subreddit), headers=headers
    )
    if not req:
        print("None")
        return
    info = req.json().get("data").get("children")
    if req.status_code != 200 or not info:
        print("None")
        return
    for hot in info:
        if i < 10:
            print(hot.get("data").get("title"))
            i = i + 1
