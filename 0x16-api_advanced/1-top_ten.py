#!/usr/bin/python3
"""Function to print the titles of the first 10 hot posts of a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return
    if response.status_code != 200:
        print(None)
        return
    
    try:
        results = response.json().get("data", {}).get("children", [])
        if not results:
            print(None)
            return
        
        for post in results:
            title = post.get("data", {}).get("title", "")
            print(title)
    except ValueError:
        print(None)


# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        top_ten(subreddit)
    else:
        print("Please provide a subreddit as an argument.")
