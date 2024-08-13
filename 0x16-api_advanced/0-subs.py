#!/usr/bin/python3
"""function that queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers."""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    api_response = requests.get(api_url, headers=request_headers, allow_redirects=False)
    if api_response.status_code == 404:
        return 0
    data = api_response.json().get("data")
    return data.get("subscribers")
