#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print("""Body response:
          \t- type: {}
          \t- content: {}"""
          .format(type(resp.text), resp.text))
