import copy
import numpy as np
from PIL import Image, ImageFilter
from moviepy.editor import VideoFileClip

VIDEO_FILE = "videos/yZqhBHPeuGc.mp4"

# video_clip = VideoFileClip(VIDEO_FILE)
# data = video_clip.get_frame(61)
# img = Image.fromarray(data, "RGB")

factor_norm = 1.05
factor_black = factor_norm * 1
img = Image.open("misc/street_light.jpg")
img.show()

mask = copy.deepcopy(img)
mask = mask.convert("L")
mask = mask.point(lambda p: 255 if p > 180 else 0)
mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
thresh = 135
mask = mask.point(lambda p: thresh + (255-thresh)*p/255 if p > thresh else 0)
mask = mask.filter(ImageFilter.GaussianBlur(radius=5))
thresh = 10
mask = mask.point(lambda p: thresh + (255-thresh)*p/255 if p > thresh else 0)
mask = mask.point(lambda p: 255 if p > 100 else p)
mask = mask.filter(ImageFilter.GaussianBlur(radius=30))
thresh = 10
# mask = mask.point(lambda p: thresh + (255-thresh)*p/255 if p > thresh else 0)
# mask = mask.point(lambda p: 255 if p > 120 else p)
mask = mask.filter(ImageFilter.BLUR)
mask.show()

for x in range(img.width):
    for y in range(img.height):
        i = img.getpixel((x, y))
        m = mask.getpixel((x, y))
        modified_pixel = tuple([min(int(factor_norm*(x*(1+m/255)) if m > 150 else factor_black*(x*(1+m/255))), 255)
                               for x in i] if m else i)
        img.putpixel((x, y), modified_pixel)

img.show()
