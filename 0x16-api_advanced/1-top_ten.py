#!/usr/bin/python3
"""Module to retrieve the top ten posts from a given subreddit."""

from requests import get


def top_ten(subreddit):
    """
    Print the titles of the top ten posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"user-agent": "MyApi/0.0.1"}
    param = {"limit": 10}
    try:
        response = get(
            url, headers=header, params=param, allow_redirects=False
        )
        response.raise_for_status()
        posts = response.json().get("data")
        [
            print(post.get("data").get("title"))
            for post in posts.get("children")
        ]
    except Exception:
        print("None")
