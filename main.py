import os
from reddit_api import get_top_posts
from audio import text_to_speech
from video import create_video
from credentials import client_id, client_secret, username, password, user_agent
import praw

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

subreddit = "TwoSentenceHorror"
num = 2
counter = 1

input_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\McBg.mp4"
output_audio_dir = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Audios"
output_video_dir = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Videos"

for post in get_top_posts(reddit, subreddit, num):
    output_audio_path = os.path.join(output_audio_dir, f"OutputAudio{counter}.mp3")
    output_video_path = os.path.join(output_video_dir, f"OutputVideo{counter}.mp4")
    
    while os.path.exists(output_audio_path) or os.path.exists(output_video_path):
        counter += 1
        output_audio_path = os.path.join(output_audio_dir, f"OutputAudio{counter}.mp3")
        output_video_path = os.path.join(output_video_dir, f"OutputVideo{counter}.mp4")
    
    text_to_speech(post.title, post.selftext, output_audio_path)
    create_video(input_video_path, output_audio_path, output_video_path)
    
    counter += 1
