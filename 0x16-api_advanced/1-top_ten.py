#!/usr/bin/python3
""" Top ten """

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        for child in children[:10]:
            post = child.get("data", {})
            print(post.get("title", None))
    except (ValueError, KeyError):
        print(None)

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
