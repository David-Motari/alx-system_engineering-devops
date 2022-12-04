#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""

import requests


url = 'http://reddit.com/r/{}/hot.json'.format(subreddit)


def count_words(subreddit, word_list, hot_list=[], after=""):
    """
    all posts recursively
    """
    headers = {'User-agent': 'karenahv'}
    params = {'t': all, 'after': after}
    req = requests.get(url, headers=headers,
                       params=params)
    if not req or req.status_code != 200:
        return None
    info = req.json()
    for hot in info['data']['children']:
        hot_list.append(hot['data']['title'])
    after = info.get('data').get('after')
    if after:
        count_words(subreddit, word_list, hot_list, after)
    return hot_list
