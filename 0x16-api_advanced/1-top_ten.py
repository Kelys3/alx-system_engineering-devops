#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10
    hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Freda Kekeli:0x16-api_advanced/1.0'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    data = response.json().get("data")
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            print(title)
