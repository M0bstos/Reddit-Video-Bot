from moviepy.editor import *
import random

def create_video(input_video_path, output_audio_path, output_video_path):
    clip = AudioFileClip(output_audio_path)
    clips = [clip]

    bg_video = VideoFileClip(input_video_path)

    duration = clip.duration

    bg_audio = bg_video.audio

    if bg_audio:
        final_audio = CompositeAudioClip([clip, bg_audio])
    else:
        final_audio = clip

    max_starting_point = bg_video.duration - duration
    starting_point = random.uniform(0, max_starting_point)

    final_video = bg_video.subclip(starting_point, starting_point + duration).set_audio(final_audio)

    final_video = final_video.resize(height=1920)
    final_video = final_video.crop(x1=1070, y1=0, x2=2350, y2=1920)
    final_video = final_video.resize(height=1080)

    final_video.write_videofile(output_video_path, fps=bg_video.fps)
