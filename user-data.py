#!/usr/bin/python3

import praw
import operator

r = praw.Reddit(user_agent='mfa_stats')
submissions = r.get_subreddit('malefashionadvice').get_hot(limit=4)
redditors = {}

for submission in submissions:
    flat_comments = praw.helpers.flatten_tree(submission.comments)

    for comment in flat_comments:
        try:
            redditor = r.get_redditor(comment.author)
            redditors[comment.author] = redditor.link_karma
        except:
            print("skipped")

    sorted_r = sorted(redditors.iteritems(), key=operator.itemgetter(1))

print(sorted_r)
