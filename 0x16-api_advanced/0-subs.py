#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'custom_user_agent'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit exists and response is OK
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        # In case of any network related errors
        return 0

# Example usage:
print(number_of_subscribers('python'))  # Should print the number of subscribers for r/python
print(number_of_subscribers('thissubredditdoesnotexist'))  # Should print 0
