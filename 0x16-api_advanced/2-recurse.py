#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query_paramt = {
        "after": after  # The query parameters
    }
    api_reqt = requests.get(
        api_url, headers={'User-Agent': 'Python/requests'}, params=query_paramt)
    try:
        api_rsp = api_reqt.json()
        article_list = api_rsp.get("data", {}).get("children", None)
        pagination_token = api_rsp.get("data", {}).get("after", None)
        if article_list is not None:
            [hot_list.append(article.get("data").get("title")) for article in article_list]
        if pagination_token is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after=pagination_token)
    except Exception:
        return None
