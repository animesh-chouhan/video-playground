import uuid
from moviepy.editor import *

audio = AudioFileClip("audios/j9oQAlTSXFQ.mp3").subclip(44, 64)
clip = ImageClip("misc/street_light.jpg").set_duration(audio.duration)
clip = clip.set_audio(audio)
clip.write_videofile("videos/{}.mp4".format(str(
    uuid.uuid4())[:7]), fps=25)
