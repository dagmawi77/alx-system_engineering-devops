#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """ Module for a function that queries the Reddit API recursively."""
    if counts is None:
        counts = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit API Example"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    if "data" in data and "children" in data["data"]:
        for post in data["data"]["children"]:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word] = counts.get(word, 0) + title.count(word.lower())
        
        if "after" in data["data"]:
            count_words(subreddit, word_list, after=data["data"]["after"], counts=counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
