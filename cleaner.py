# Import regex tools
import re

def clean_tweets(tweets, col_name, emoji_regex):
    # Remove links
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('https?:\/\/t\.co\/[\w]{8,8}'), '', x))
    # Remove usernames
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('@[A-Za-z0-9_]+'), '', x))
    # Remove newline character
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('[\n\r]+'), '', x))
    # Insert space between emojis
    #tweets[col_name] = tweets[col_name].map(lambda x: re.sub(emoji_regex, r' \1 ', x))
    # Replace multiple spaces with single one
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('[\s]+'), ' ', x))
    return tweets
