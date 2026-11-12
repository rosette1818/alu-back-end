#!/usr/bin/python3
"""Query the Reddit API and return the subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for a given subreddit, or 0 if invalid."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)
