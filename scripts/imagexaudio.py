import uuid
from moviepy.editor import *

AUDIO_PATH = "audios/j9oQAlTSXFQ.mp3"
IMAGE_PATH = "misc/street_light_mobile.jpg"

duration = 12
start = 49
end = start + duration
audio = AudioFileClip(AUDIO_PATH).subclip(start, end)
clip = ImageClip(IMAGE_PATH).set_duration(audio.duration)
clip = clip.set_audio(audio)
clip.write_videofile("videos/{}_{}.mp4".format(str(
    uuid.uuid4())[:7], str(duration)), fps=25)
