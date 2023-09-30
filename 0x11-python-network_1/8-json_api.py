#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter 'q' as a parameter.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    values = {"q": q}
    resp = requests.post(url, data=values)
    try:
        val_json = resp.json()
        if val_json:
            print(f"[{val_json['id']}] {val_json['name']}")
        else:
            print("No result")
    except requests.exceptions.InvalidJSONError:
        print("Not a valid JSON")
