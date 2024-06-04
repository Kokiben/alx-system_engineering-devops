#!/usr/bin/python3
"""function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    if response.status_code != 200:
        return 0
    results = response.json().get("data", {})
    return results.get("subscribers", 0)


# Example usage:
if __name__ == "__main__":
    print(number_of_subscribers('programming'))  # Should print the number of subscribers for r/programming
    print(number_of_subscribers('thissubredditdoesnotexist'))  # Should print 0
