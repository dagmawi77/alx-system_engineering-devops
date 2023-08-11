#!/usr/bin/python3
"""
Defines a function that queries Reddit API
"""
import requests
import json

def count_words(subreddit, word_list):
    if not word_list:
        # Reached the end of the word list, print the results
        print(*sorted(word_counts.items(), key=lambda x: (-x[1], x[0])), sep="\n")
        return

    # Get the hot articles for the subreddit
    response = requests.get(f"https://api.reddit.com/r/{subreddit}/hot")
    if response.status_code != 200:
        # The subreddit is invalid, do nothing
        return

    # Parse the JSON response
    articles = json.loads(response.content)

    # Loop over the articles
    for article in articles["data"]["children"]:
        # Get the title of the article
        title = article["data"]["title"].lower()

        # Check if the title contains any of the keywords
        for word in word_list:
            if word in title:
                # If it does, count the word
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    # Recursively call the function with the remaining words
    count_words(subreddit, word_list[1:])

if __name__ == "__main__":
    word_list = sys.argv[2].split()
    count_words(sys.argv[1], word_list)
