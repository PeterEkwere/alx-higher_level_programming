#!/usr/bin/python3
"""
    This scripts sends request using the request package
    Author: Peter Ekwere
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    parameter = {'email': mail}
    response = requests.post(url, data=parameter)
    print(response.text)
