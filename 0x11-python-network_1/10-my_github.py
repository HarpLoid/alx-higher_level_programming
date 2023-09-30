#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    headers = {'Authorization': f'Bearer {token}'}

    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        print(resp.json()["id"])
    except requests.exceptions.HTTPError:
        print("None")
        exit()
