#!/usr/bin/python3
"""
    This script takes in a letter and sends a POST request to
    Author: Peter Ekwere
"""
import requests
import sys


if __name__ == "__main__":
    try:
        url = "http://0.0.0.0:5000/search_user"
        if sys.argv[1]:
            q = sys.argv[1]
        else:
            q = ""
        response = requests.post(url, data={'q': q})
        json_data = response.json()
        if not json_data:
            print("no result")
        print(f"[{json_data.get('id')}] {json_data['name']}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
