#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    return  the number of subscribers.
    """
    api_reqts = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if api_reqts.status_code == 200:
        return api_reqts.json().get("data").get("subscribers")
    else:
        return 0
