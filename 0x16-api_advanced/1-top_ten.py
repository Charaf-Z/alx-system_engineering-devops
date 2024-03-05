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
    header = {"user-agent": "Webkit:api.advanced:v1.0.0 Htk like Gecko"}
    param = {"limit": 10}
    response = get(url, headers=header, params=param, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    posts = response.json().get("data")
    [print(post.get("data").get("title")) for post in posts.get("children")]
