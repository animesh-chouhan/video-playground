import os
import copy
import numpy as np
from moviepy.editor import *
from PIL import Image, ImageFilter
from extract_audio import extract_audio
from analyse_audio import get_audio_mask

VIDEO_FILE = "videos/yZqhBHPeuGc-050ecec.mp4"
AUDIO_SAMPLE_RATE = 44100


def video_filter(get_frame, t):
    frame = get_frame(t)

    factor = 1 + abs(AUDIO_MASK[int(AUDIO_SAMPLE_RATE*t)])
    img = Image.fromarray(frame, "RGB")

    mask = copy.deepcopy(img)
    mask = mask.convert("L")
    mask = mask.point(lambda p: 255 if p > 180 else 0)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
    mask = mask.point(lambda p: 255 if p > 10 else 0)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=10))
    mask = mask.point(lambda p: 255 if p > 10 else 0)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=10))
    mask = mask.filter(ImageFilter.BLUR)

    for x in range(img.width):
        for y in range(img.height):
            i = img.getpixel((x, y))
            m = mask.getpixel((x, y))
            modified_pixel = tuple([int(factor*(x*(1+m/255)))
                                    for x in i] if m else i)
            img.putpixel((x, y), modified_pixel)

    return np.asarray(img)


audio_file_path = extract_audio(VIDEO_FILE)
AUDIO_MASK = get_audio_mask(audio_file_path)

video_clip = VideoFileClip(VIDEO_FILE)
modified_video_clip = video_clip.fl(video_filter)

modified_video_clip.write_videofile(
    os.path.join("generated", "generated.mp4"), threads=10)