#!/usr/bin/python3
"""Query the Reddit API and print the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit, or None."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
