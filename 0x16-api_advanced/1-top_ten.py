#!/usr/bin/python3
"""Get the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json().get('data')
        if data is None:
            print(None)
            return
        
        posts = data.get('children')
        if not posts:
            print(None)
            return
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    
    except requests.RequestException:
        print(None)
