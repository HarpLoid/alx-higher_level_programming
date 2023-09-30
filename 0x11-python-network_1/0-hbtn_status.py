#!/usr/bin/python3
"""
Fetches "https://alx-intranet.hbtn.io/status"
"""
import urllib.request


if __name__ == "__main__":
    url = 'http://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("""Body response:
              \t- type: {}
              \t- content: {}
              \t- utf8 content: {}"""
              .format(type(html), html, html.decode('utf8')))
