#!/usr/bin/python3
"""Module to count occurrences of words in titles of posts from a subreddit."""

from requests import get


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Count occurrences of words in titles of posts from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count occurrences
                of in post titles.
        instances (dict, optional): A dictionary to store word occurrences.
        after (str, optional): Parameter to paginate through posts.
        count (int, optional): Total number of posts processed.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"user-agent": "alx:0x16.api.advanced:v1.0.0"}
    param = {"limit": 100, "after": after, "count": count}
    response = get(url, headers=header, params=param, allow_redirects=False)
    try:
        results = response.json()
        if response.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return
    posts = results.get("data")
    after = posts.get("after")
    count += posts.get("dist")
    for post in posts.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times
    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
