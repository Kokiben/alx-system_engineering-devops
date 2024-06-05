#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], ftr=None):
    """  returns a list containing the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hdrs = {'User-Agent': 'my-app/0.0.1'}
    prsms = {'after': ftr} if ftr else {}

    rps = requests.get(url, headers=hdrs, params=prsms, allow_redirects=False)

    if rps.status_code != 200:
        return None

    try:
        dat = rps.json().get("data", {})
        pst = dat.get("children", [])
        for p in pst:
            pot = p.get("data", {})
            hot_list.append(pot.get("title", None))

        ftr = dat.get("after", None)
        if ftr:
            return recurse(subreddit, hot_list, ftr)
        return hot_list
    except (ValueError, KeyError):
        return None


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        rslt = recurse(sys.argv[1])
        if rslt is not None:
            print(len(rslt))
        else:
            print("None")
