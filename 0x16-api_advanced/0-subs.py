#!/usr/bin/python3
"""fun tion for Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Gets number of subcribers from a given subredit"""
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    res = requests.get(url, headers=header)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    pass
