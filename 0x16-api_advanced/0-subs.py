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
    header = {"User-Agent": "Alx:0x16.api.advanced"}
    response = get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
