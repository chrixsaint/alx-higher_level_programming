#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL, and
displays the value of the X-Request-Id variable found in the header
of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
