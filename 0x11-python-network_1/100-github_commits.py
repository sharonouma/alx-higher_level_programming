#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url).json()
    for i in range(10):
        print("{}: {}".format(
            r[i].get('sha'), r[i].get('commit').get('author').get('name')))
