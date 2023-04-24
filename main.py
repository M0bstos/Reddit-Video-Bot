import praw
import pyttsx3
from moviepy.editor import *
import random

input_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\McBg.mp4"
output_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Videos\OutputVideo.mp4"

reddit = praw.Reddit(
    client_id='yIsDqV27uW8MZ5_EKvfRkg',
    client_secret='Kke_vXS-XoSGxqt0Ro0Ru6G6Vf8ojg',
    username='M0bstos',
    password='1211harsh',
    user_agent='projectmonkey/1.0'
)

engine = pyttsx3.init()

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)

subreddit = "TwoSentenceHorror"
num = 1

subreddit = reddit.subreddit(subreddit)

clips = []

for post in subreddit.top(limit=num):
    title = post.title
    content = post.selftext
    print("Title: ", title)
    engine.say(title)
    if content:
        print("Content: ", content)
        engine.say(content)

final = title
if content:
    final += " " + content

engine.save_to_file(final,r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Audios\OutputAudio.mp3")
engine.runAndWait()

clip = AudioFileClip(r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Audios\OutputAudio.mp3")
clips.append(clip)

audio = concatenate_audioclips(clips)

bg_video = VideoFileClip(input_video_path)

duration = audio.duration
bg_video = bg_video.subclip(0, duration)

bg_audio = bg_video.audio

if bg_audio:
    final_audio = CompositeAudioClip([audio, bg_audio])
else:
    final_audio = audio

final_video = bg_video.set_audio(final_audio)

final_video = final_video.resize(height=1080)
final_video = final_video.crop(x1=420, y1=0, x2=1500, y2=1080)

final_video.write_videofile(output_video_path, fps=bg_video.fps)