import praw
from credentials import client_id, client_secret, username, password, user_agent

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)


def get_top_posts(reddit, subreddit, num_posts=2, time_filter='day'):
    subreddit = reddit.subreddit(subreddit)
    top_posts = subreddit.top(time_filter=time_filter, limit=num_posts)
    return list(top_posts)
