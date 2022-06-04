import os
import copy
import numpy as np
import concurrent.futures
from moviepy.editor import *
from PIL import Image, ImageFilter
from extract_audio import extract_audio
from analyse_audio import get_audio_mask

VIDEO_FILE = "videos/7665910.mp4"
AUDIO_SAMPLE_RATE = 44100


# def video_filter(frame, index):
#     print("Processing frame: {}".format(index))
#     # factor = 1 + abs(AUDIO_MASK[int(AUDIO_SAMPLE_RATE*t)])
#     factor = 1
#     img = Image.fromarray(frame, "RGB")

#     mask = copy.deepcopy(img)
#     mask = mask.convert("L")
#     mask = mask.point(lambda p: 255 if p > 180 else 0)
#     mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
#     thresh = 135
#     mask = mask.point(lambda p: thresh + (255-thresh)
#                       * p/255 if p > thresh else 0)
#     mask = mask.filter(ImageFilter.GaussianBlur(radius=5))
#     thresh = 10
#     mask = mask.point(lambda p: thresh + (255-thresh)
#                       * p/255 if p > thresh else 0)
#     mask = mask.point(lambda p: 255 if p > 100 else p)
#     mask = mask.filter(ImageFilter.GaussianBlur(radius=30))
#     thresh = 10
#     mask = mask.filter(ImageFilter.BLUR)

#     for x in range(img.width):
#         for y in range(img.height):
#             i = img.getpixel((x, y))
#             m = mask.getpixel((x, y))
#             modified_pixel = tuple([min(int(factor*(x*(1+m/255)) if m > 150 else factor*(x*(1+m/255))), 255)
#                                     for x in i] if m else i)
#             img.putpixel((x, y), modified_pixel)

#     return np.asarray(img)

def video_filter(frame, index):
    print("Processing frame: {}".format(index))
    return frame


audio_file_path = extract_audio(VIDEO_FILE)
AUDIO_MASK = get_audio_mask(audio_file_path)

video_clip = VideoFileClip(VIDEO_FILE)
duration = video_clip.duration
fps = video_clip.fps
timestamps = np.linspace(0, duration, int(duration*fps))

frames = []

for t in timestamps:
    frames.append(video_clip.get_frame(t))

with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    gen = executor.map(
        video_filter, frames, list(range(len(frames))))

processed_frames = list(gen)
print(type(processed_frames[0]))
final_clip = ImageSequenceClip(processed_frames, fps=fps)
final_clip.write_videofile(os.path.join("generated", "generated.mp4"), fps=fps)

# new_frames = [frame for frame in video_clip.iter_frames()]
# print(type(new_frames[0]))
# new_clip = ImageSequenceClip(new_frames, fps=video_clip.fps)
# new_clip.write_videofile("new_file.mp4")
