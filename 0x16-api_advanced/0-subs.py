#!/usr/bin/python3
"""Module to retrieve the number of subscribers for a given subreddit."""

from requests import get


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Return:
        int: The number of subscribers of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alx:0x16.api.advanced:v1.0.0"}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
