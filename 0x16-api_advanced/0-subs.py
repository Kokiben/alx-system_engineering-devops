#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hadrs = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    rps = requests.get(url, headers=hadrs, allow_redirects=False)
    if rps.status_code == 404:
        return 0
    if rps.status_code != 200:
        return 0
    rlts = response.json().get("data", {})
    return rlts.get("subscribers", 0)


# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
    else:
        print("Please provide a subreddit as an argument.")
