#!/usr/bin/python3
"""function that queries the Reddit API"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    hdrs = {'user-agent': 'my-app/0.0.1'}

    rps = requests.get(url, headers=hdrs, allow_redirects=False)

    if rps.status_code != 200:
        print(None)
        return

    try:
        dat = rps.json().get("data", {})
        pst = dat.get("children", [])
        for p in pst[:10]:
            pot = p.get("data", {})
            print(pot.get("title", None))
    except (ValueError, KeyError):
        print(None)

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
