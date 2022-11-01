#!/usr/bin/python3
"""function for Reddit API."""
import requests


def top_ten(subreddit):
    """Gets top 10 posts from a given subredit"""
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    res = requests.get(url, headers=header)
    if res.status_code == 200:
        for i in res.json()["data"]["children"]:
            print(i["data"]["title"])
    else:
        return None


if __name__ == "__main__":
    pass
