import os
from moviepy.editor import *


def extract_audio(video_file_path):
    video_file_name = os.path.basename(video_file_path)
    print("Video file: " + video_file_name)

    audio_file_name = video_file_name.split(".")[-2] + ".mp3"
    audio_file_path = os.path.join("audios", audio_file_name)

    if not os.path.exists(audio_file_path):
        with AudioFileClip(video_file_path) as audioclip:
            audioclip.write_audiofile(audio_file_path)
    else:
        print("Audio file already exists.")

    return audio_file_path
