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
    header = {"User-Agent": "Alx:0x16.api.advanced"}
    param = {"limit": 10}
    response = get(url, headers=header, params=param, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    posts = response.json().get("data")
    [print(post.get("data").get("title")) for post in posts.get("children")]