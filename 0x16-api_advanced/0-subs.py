#!/usr/bin/python3
"""function that queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Setting a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditSubscriberChecker/1.0)'}
    
    try:
        # Sending GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0
            return 0
    except requests.exceptions.RequestException:
        # In case of any request-related errors, return 0
        return 0
