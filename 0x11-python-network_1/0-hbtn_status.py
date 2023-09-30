#!/usr/bin/python3
"""
Fetches "https://alx-intranet.hbtn.io/status"
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('http://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("""Body response:
              \t- type: {}
              \t- content: {}
              \t- utf8 content: {}"""
              .format(type(html), html, html.decode('utf8')))
