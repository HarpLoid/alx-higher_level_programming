#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter 'q' as a parameter.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://736def419d41.6e431165.alx-cod.online:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    values = {"q": q}
    resp = requests.post(url, data=values)
    try:
        val_json = resp.json()
        print(val_json)
        if val_json:
            print(f"[{val_json['id']}] {val_json['name']}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
