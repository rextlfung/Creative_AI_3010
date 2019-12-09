import praw
import pdb
import re
import os
import random
from creative_ai.reddit.wavLinks import *

def reddit_write():
    reddit = praw.Reddit('bot1')

    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    subreddit = reddit.subreddit('gaming')
    for submission in subreddit.hot(limit=100):
        if submission.id not in posts_replied_to:
            if re.search("music", submission.title, re.IGNORECASE):
                path = 'C:\\EECS_Projects/Creative_AI_3010_Repository/creative_ai/wav'
                submission.reply("Speaking of music, what do you think of this new song that I made?\n"
                 + random.choice(links))
                print("Bot replying to : ", submission.title)
                posts_replied_to.append(submission.id)
                break

    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
