#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import json
import requests


def count_words(subreddit, word_list, pagination_token="", word_count=[]):
    """Count occurrences of specified words in hot posts of a subreddit."""

    if pagination_token == "":
        word_count = [0] * len(word_list)

    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        api_url,
        params={'after': pagination_token},
        allow_redirects=False,
        headers={'User-Agent': 'bhalut'}
    )

    if response.status_code == 200:
        api_response = response.json()

        for post in api_response['data']['children']:
            for word in post['data']['title'].split():
                for a in range(len(word_list)):
                    if word_list[a].lower() == word.lower():
                        word_count[a] += 1

        pagination_token = api_response['data']['after']
        if pagination_token is None:
            # Merge counts for duplicate words
            merged_indices = []
            for a in range(len(word_list)):
                for b in range(a + 1, len(word_list)):
                    if word_list[a].lower() == word_list[b].lower():
                        merged_indices.append(b)
                        word_count[b] += word_count[b]

            # Sort words by count and alphabetically
            for a in range(len(word_list)):
                for b in range(a, len(word_list)):
                    if (word_count[b] > word_count[a] or
                            (word_list[a] > word_list[b] and
                             word_count[b] == word_count[a])):
                        # Swap counts and words
                        word_count[a], word_count[b] = word_count[b], word_count[a]
                        word_list[a], word_list[b] = word_list[b], word_list[a]

            # Print results
            for a in range(len(word_list)):
                if (word_count[a] > 0) and a not in merged_indices:
                    print("{}: {}".format(word_list[a].lower(), word_count[a]))
        else:
            count_words(subreddit, word_list, pagination_token, word_count)
