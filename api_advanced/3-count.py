#!/usr/bin/python3
"""Recursively query Reddit hot titles and count keyword occurrences."""
import requests


def _count_in_words(words, target, idx=0):
    """Recursively count exact matches of target in a list of words."""
    if idx >= len(words):
        return 0
    match = 1 if words[idx] == target else 0
    return match + _count_in_words(words, target, idx + 1)


def _count_in_titles(titles, counts, multipliers, idx=0):
    """Recursively update keyword counts across all fetched titles."""
    if idx >= len(titles):
        return
    words = titles[idx].lower().split()

    def _update_keys(keys, k_idx=0):
        if k_idx >= len(keys):
            return
        key = keys[k_idx]
        occurrences = _count_in_words(words, key)
        if occurrences:
            counts[key] += occurrences * multipliers[key]
        _update_keys(keys, k_idx + 1)

    _update_keys(list(counts.keys()))
    _count_in_titles(titles, counts, multipliers, idx + 1)


def _init_dicts(word_list, counts, multipliers, idx=0):
    """Recursively initialize keyword counts and duplicate multipliers."""
    if idx >= len(word_list):
        return
    word = word_list[idx].lower()
    counts[word] = 0
    multipliers[word] = multipliers.get(word, 0) + 1
    _init_dicts(word_list, counts, multipliers, idx + 1)


def _print_results(sorted_items, idx=0):
    """Recursively print sorted keyword counts greater than zero."""
    if idx >= len(sorted_items):
        return
    word, total = sorted_items[idx]
    if total > 0:
        print("{}: {}".format(word, total))
    _print_results(sorted_items, idx + 1)


def count_words(subreddit, word_list, after=None, titles=None):
    """Query all hot posts recursively and print sorted keyword counts."""
    if not subreddit or not isinstance(subreddit, str) or not word_list:
        return

    if titles is None:
        titles = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    def _collect_titles(c_idx=0):
        if c_idx >= len(children):
            return
        titles.append(children[c_idx].get("data", {}).get("title", ""))
        _collect_titles(c_idx + 1)

    _collect_titles()

    next_after = data.get("after")
    if next_after is not None:
        count_words(subreddit, word_list, next_after, titles)
        return

    counts = {}
    multipliers = {}
    _init_dicts(word_list, counts, multipliers)
    _count_in_titles(titles, counts, multipliers)

    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    _print_results(sorted_items)
