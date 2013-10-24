#!/usr/bin/python3

import praw
import shelve

# Where we store our data
d = shelve.open('reddit_data')

r = praw.Reddit(user_agent='mfa_stats')
submissions = r.get_subreddit('malefashionadvice').get_hot(limit=None)

for submission in submissions:
    vals = {}
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    vals['comments'] = flat_comments
    vals['url'] = submission.url
    vals['title'] = submission.title
    vals['author'] = submission.author.name

    d[submission.title + " " + str(submission.created)] = vals

d.close()
