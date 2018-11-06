import praw
import config

reddit = praw.Reddit(client_id=config.RedditClientId,
                     client_secret=config.RedditClientSecret,
                     user_agent='my user agent')

# Output 10 submitions
for submission in reddit.subreddit('wallstreetbets').hot(limit=10):
    print(submission.title)
