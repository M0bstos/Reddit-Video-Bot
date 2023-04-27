from credentials import client_id, client_secret, username, password, user_agent
from reddit_api import get_top_post
from audio import text_to_speech
from video import create_video
import os

counter = 1

input_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\McBg.mp4"
output_audio_dir = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Audios"
output_video_dir = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Videos"

subreddit = "TwoSentenceHorror"
num = 1

post = get_top_post(subreddit)

output_audio_path = os.path.join(output_audio_dir, f"OutputAudio{counter}.mp3")

text_to_speech(post.title, post.selftext, output_audio_path)

create_video(input_video_path, output_audio_path, os.path.join(output_video_dir, f"OutputVideo{counter}.mp4"))

counter += 1
