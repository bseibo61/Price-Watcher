import praw

reddit = praw.Reddit(client_id='q7Vwxwy_u5H2yQ',
                     client_secret='FLhk_nNnZtbh6VZay3IOiXKbjjQ',
                     user_agent='my user agent')

# Output 10 submitions
for submission in reddit.subreddit('wallstreetbets').hot(limit=10):
    print(submission.title)
