#!/usr/bin/python3
"""
Script that takes a letter and post request to url/search_user
"""

import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    data = {'q': q}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data).json()
        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r.get('id'), r.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
