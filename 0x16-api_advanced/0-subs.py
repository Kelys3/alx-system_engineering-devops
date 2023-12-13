#!/usr/bin/python3
"""A function that queries the Reddit API and returns the total number
of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Freda Kekeli:0x16-api_advanced/1.0'}

    response = requests.get(url, headers=headers).json()

    subs_count = response.get("data", {}).get("subscribers", 0)

    return subs_count
