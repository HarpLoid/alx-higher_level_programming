#!/bin/bash
# Takes in a URL as an argument, Sends a GET request to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
