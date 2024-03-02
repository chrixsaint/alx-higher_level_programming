#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
do this - ./10-my_github.py <GitHub username> <GitHub password>
would u se Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))