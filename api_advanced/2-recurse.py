#!/usr/bin/python3
"""Recursively query the Reddit API for all hot article titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles for a subreddit, or None."""
    if not subreddit or not isinstance(subreddit, str):
        return None

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after is not None:
        return recurse(subreddit, hot_list, next_after)

    return hot_list if hot_list else None
