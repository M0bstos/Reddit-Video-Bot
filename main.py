import praw
import pyttsx3
from moviepy.editor import *
import random
import os

counter= 1

input_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\McBg.mp4"

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
num = 2

subreddit = reddit.subreddit(subreddit)

for post in subreddit.top(limit=num):

    output_audio_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Audios\OutputAudio{}.mp3".format(counter)
    output_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Videos\OutputVideo{}.mp4".format(counter)

    while os.path.exists(output_audio_path) or os.path.exists(output_video_path):
        counter += 1
        output_audio_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Audios\OutputAudio{}.mp3".format(counter)
        output_video_path = r"C:\Users\Harsh Nanda\OneDrive\Desktop\STUFF\Reddit-Video-Bot\Output Videos\OutputVideo{}.mp4".format(counter)

    clips = []

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

    engine.save_to_file(final,output_audio_path)
    engine.runAndWait()

    clip = AudioFileClip(output_audio_path)
    clips.append(clip)

    audio = concatenate_audioclips(clips)

    bg_video = VideoFileClip(input_video_path)

    duration = audio.duration

    bg_audio = bg_video.audio

    if bg_audio:
        final_audio = CompositeAudioClip([audio, bg_audio])
    else:
        final_audio = audio

    max_starting_point = bg_video.duration - duration
    starting_point = random.uniform(0, max_starting_point)

    final_video = bg_video.subclip(starting_point, starting_point + duration).set_audio(final_audio)

    final_video = final_video.resize(height=1080)
    final_video = final_video.crop(x1=420, y1=0, x2=1500, y2=1080)

    final_video.write_videofile(output_video_path, fps=bg_video.fps)

    counter += 1