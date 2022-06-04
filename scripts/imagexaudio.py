import uuid
from moviepy.editor import *

duration = 20
start = 46
end = start + duration
audio = AudioFileClip("audios/j9oQAlTSXFQ.mp3").subclip(start, end)
clip = ImageClip("misc/street_light_mobile.jpg").set_duration(audio.duration)
clip = clip.set_audio(audio)
clip.write_videofile("videos/{}_{}.mp4".format(str(
    uuid.uuid4())[:7], str(duration)), fps=25)
