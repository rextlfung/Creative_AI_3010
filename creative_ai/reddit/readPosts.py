import praw

def reddit_test():
    reddit = praw.Reddit('bot1')

    subreddit = reddit.subreddit("learnpython")

    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")
