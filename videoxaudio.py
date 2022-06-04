import uuid
from moviepy.editor import *

videoclip = VideoFileClip("videos/AGrTcMsLGWY-49ec8eb.mp4")
audioclip = AudioFileClip("audios/j9oQAlTSXFQ.mp3").subclip(44, 64)
videoclip = videoclip.set_audio(audioclip)
videoclip.write_videofile("videos/{}.mp4".format(str(
    uuid.uuid4())[:7]), fps=25)
