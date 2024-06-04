#!/usr/bin/python3
""" Count it! """
import json
import requests


def count_words(subreddit, word_list, posts=None, word_counts=None):
    if posts is None:
        posts = []
    if word_counts is None:
        word_counts = {}

    if not subreddit:
        print("Invalid subreddit or no posts found.")
        return

    if len(posts) == 0:
        reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                             client_secret='YOUR_CLIENT_SECRET',
                             user_agent='YOUR_USER_AGENT')

        try:
            hot_posts = reddit.subreddit(subreddit).hot(limit=100)
            for post in hot_posts:
                posts.append(post.title.lower())
        except:
            print("Invalid subreddit or no posts found.")
            return

    if len(posts) == 0:
        print("No posts found.")
        return

    if len(word_list) == 0:
        for word, count in sorted(word_counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"{word}: {count}")
        return

    word = word_list[0].lower()
    word_counts[word] = sum(post.count(word) for post in posts)
    count_words(subreddit, word_list[1:], posts, word_counts)

count_words('programming', ['react', 'python', 'java', 'javascript', 'scala', 'no_results_for_this_one'])
