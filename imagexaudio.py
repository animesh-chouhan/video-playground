from moviepy.editor import *

audio = AudioFileClip("audios/6YAWKYYBYCY-08e2c88.mp3")
clip = ImageClip("misc/lights.jpg").set_duration(audio.duration)
clip = clip.set_audio(audio)
clip.write_videofile("videos/render.mp4", fps=25)
