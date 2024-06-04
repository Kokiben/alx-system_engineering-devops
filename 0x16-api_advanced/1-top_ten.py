#!/usr/bin/python3
"""
Function that queries the Reddit API and
prints the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    headers = {'User-Agent': 'Python/requests'}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print(None)
        return

    try:
        resp = response.json()
        posts = resp.get("data", {}).get("children", None)
        if posts is None:
            print(None)
        else:
            for post in posts:
                print(post.get("data", {}).get("title", None))
    except (ValueError, KeyError):
        print(None)


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
