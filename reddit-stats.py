#!/usr/bin/python3

import praw
import shelve

# Where we store our data
d = shelve.open('reddit_data')

# a list of all existing keys (slow!)
values = d.values()

for v in values:
    print(v)
    break
    flat_comments = praw.helpers.flatten_tree(submission.comments)

    # for comment in flat_comments:
    #     if 'trade' in comment:
    #         print(comment)
