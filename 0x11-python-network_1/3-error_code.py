#!/usr/bin/python3
"""
script that takes in url and sends a request to url
displays body of response
"""

import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode(encoding="utf-8"))
    except URLError as err:
        print("Error code: {}".format(err.code))
