#!/usr/bin/python3
"""Reddit API"""

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
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        word_count[i] += 1

        pagination_token = api_response['data']['after']
        if pagination_token is None:
            # Merge counts for duplicate words
            merged_indices = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        merged_indices.append(j)
                        word_count[i] += word_count[j]

            # Sort words by count and alphabetically
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (word_count[j] > word_count[i] or
                            (word_list[i] > word_list[j] and
                             word_count[j] == word_count[i])):
                        # Swap counts and words
                        word_count[i], word_count[j] = word_count[j], word_count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            # Print results
            for i in range(len(word_list)):
                if (word_count[i] > 0) and i not in merged_indices:
                    print("{}: {}".format(word_list[i].lower(), word_count[i]))
        else:
            count_words(subreddit, word_list, pagination_token, word_count)
