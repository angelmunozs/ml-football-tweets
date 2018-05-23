# Import regex tools
import re

# Import custom emoji regex pattern
from emoji_regex import emoji_regex

def clean_tweets(tweets, col_name):
    # Remove links
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('https?:\/\/t\.co\/[\w]{8,8}'), '', x))
    # Remove usernames
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('@[A-Za-z0-9_]+'), '', x))
    # Remove newline character
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('[\n\r]+'), '', x))
    # Replace multiple spaces with single one
    tweets[col_name] = tweets[col_name].map(lambda x: re.sub(re.compile('[\s]+'), ' ', x))
    # Remove emojis
    #tweets[col_name] = tweets[col_name].map(lambda x: re.sub(emoji_regex, ' ', x))
    return tweets
