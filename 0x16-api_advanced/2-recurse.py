#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return a list containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        for child in children:
            post = child.get("data", {})
            hot_list.append(post.get("title", None))

        after = data.get("after", None)
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except (ValueError, KeyError):
        return None


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
