#!/usr/bin/python3
"""  recursive function that queries the Reddit API """
from requests import get

RDDT = "https://www.reddit.com/"
HDRS = {'user-agent': 'my-app/0.0.1'}

def count_words(subreddit, word_list, ftr="", ftr_di={}):
    """title of all hot articles, and prints a sorted count """
    if not ftr_di:
        for f in word_list:
            ftr_di[f] = 0

    if ftr is None:
        word_list = [[key, value] for key, value in ftr_di.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for wo in word_list:
            if wo[1]:
                print("{}: {}".format(wo[0].lower(), wo[1]))
        return None

    url = RDDT + "r/{}/hot/.json".format(subreddit)

    pras = {
        'limit': 100,
        'after': ftr
    }

    rps = get(url, headers=HDRS, params=pras, allow_redirects=False)

    if rps.status_code != 200:
        return None

    try:
        s = rps.json()
    except ValueError:
        return None

    try:
        dat = s.get("data")
        ftr = dat.get("after")
        pst = dat.get("children")
        for p in pst:
            pot = p.get("data")
            tltl = pot.get("title")
            lwr = [l.lower() for l in tltl.split(' ')]

            for wo in word_list:
                ftr_di[wo] += lwr.count(wo.lower())

    except:
        return None

    return count_words(subreddit, word_list, ftr, ftr_di)

count_words('programming', ['react', 'python', 'java', 'javascript', 'scala', 'no_results_for_this_one'])
