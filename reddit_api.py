import praw
from credentials import client_id, client_secret, username, password, user_agent

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

def get_top_post(subreddit, time_filter='day'):
    subreddit = reddit.subreddit(subreddit)
    return subreddit.top(time_filter=time_filter, limit=1).__next__()
