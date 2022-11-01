#!/usr/bin/python3
"""function for Reddit API."""
import requests


after = ""


def recurse(subreddit, hot_list=[]):
    """Gets hot posts from a given subredit"""
    global after
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    if after:
        url = url + "?after=" + after

    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code == 200:
        for i in res.json().get("data", None).get("children", None):
            hot_list.append(i.get("data", None).get("title", None))
    else:
        return None

    after = res.json().get("after", "")
    if after:
        return recurse(subreddit, hoy_list)
    return hot_list


if __name__ == "__main__":
    pass
