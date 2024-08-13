#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    paramt = {
        'limit': 10
    }
    api_reqt = requests.get(
        api_url, headers={'User-Agent': 'Python/requests'}, params=paramt)

    try:
        resp = api_reqt.json()
        qui_po = resp.get("data", {}).get("children", None)
        if qui_po is None:
            print(None)
        else:
            [print(po.get("data").get("title")) for po in qui_po]
    except Exception:
        print(None)
