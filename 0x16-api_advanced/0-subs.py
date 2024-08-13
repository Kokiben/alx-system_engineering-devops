#!/usr/bin/python3
"""function that queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return 0

    # Parse the response and get the number of subscribers
    results = response.json().get("data")
    if results is None:
        return 0
    return results.get("subscribers", 0)
