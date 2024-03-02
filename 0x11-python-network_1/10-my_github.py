#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and personal access
token) and uses the GitHub API to display your id.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        token = sys.argv[2]

        url = "https://api.github.com/user"
        headers = {"Authorization": "Basic " + username + ":" + token}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data.get("id"))
        else:
            print(None)
