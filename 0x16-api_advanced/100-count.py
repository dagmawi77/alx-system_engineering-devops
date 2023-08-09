#!/usr/bin/python3
"""recursive function that queries the Reddit API,
   """
import requests
from sys import argv
after = None
count_dic = []


def count_words(subreddit, word_list):
    """function queries reddit api"""
    global after
    global count_dic
    headers = {'User-Agent': 'xica369'}
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(URL, headers=headers, allow_redirects=False,
                            params=parameters)
