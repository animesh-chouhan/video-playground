import os
import uuid
from moviepy.editor import VideoFileClip

VIDEO_FILE = "videos/AGrTcMsLGWY.mp4"


head, tail = os.path.split(VIDEO_FILE)
clip = VideoFileClip(VIDEO_FILE).subclip(61, 81)
clip.write_videofile(os.path.join(head, tail.split(".")[-2] + "-" + str(
    uuid.uuid4())[:7] + ".mp4"), codec="libx264")
