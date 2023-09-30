#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        resp = requests.get(argv[1])
        resp.raise_for_status()
        print(resp.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(resp.status_code))
