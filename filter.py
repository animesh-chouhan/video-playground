import copy
import numpy as np
from PIL import Image, ImageFilter
from moviepy.editor import VideoFileClip

VIDEO_FILE = "videos/yZqhBHPeuGc.mp4"

# video_clip = VideoFileClip(VIDEO_FILE)
# data = video_clip.get_frame(61)
# img = Image.fromarray(data, "RGB")

factor_norm = 1.03
factor_black = factor_norm * 1
img = Image.open("misc/street_light.jpg")
# img.show()
# np.interp(0.3, [0,0.5], [1,1.05])

mask = copy.deepcopy(img)
mask = mask.convert("L")
mask = mask.point(lambda p: 255 if p > 170 else 0)
mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
mask = mask.point(lambda p: 255 if p > 50 else 0)
mask = mask.filter(ImageFilter.GaussianBlur(radius=20))
pix = np.array(mask)
# mask.show()
# mask = mask.point(lambda p: np.interp(p, [10, 220], [0, 255]))
pix = np.array(mask)
mask = mask.filter(ImageFilter.BLUR)
mask.show()

# for i in range(256):
#     print(i, np.count_nonzero(pix==i))
# thresh = 40
# mask = mask.point(interpolate)
# mask = mask.filter(ImageFilter.GaussianBlur(radius=5))
# mask = mask.point(lambda p: 255 if p > 40 else 0)
# mask = mask.point(lambda p: 255 if p > 20 else 0)
# thresh = 10
# mask = mask.point(interpolate)

# thresh = 135
# mask = mask.point(lambda p: thresh + (255-thresh)*p/255 if p > thresh else 0)
# mask = mask.filter(ImageFilter.GaussianBlur(radius=5))
# thresh = 10
# mask = mask.point(lambda p: thresh + (255-thresh)*p/255 if p > thresh else 0)
# mask = mask.point(lambda p: 255 if p > 100 else p)
# mask = mask.filter(ImageFilter.GaussianBlur(radius=30))
# thresh = 10
# mask = mask.point(lambda p: thresh + (255-thresh)*p/255 if p > thresh else 0)
# mask = mask.point(lambda p: 255 if p > 120 else p)
# mask = mask.filter(ImageFilter.BLUR)


for x in range(img.width):
    for y in range(img.height):
        i = img.getpixel((x, y))
        m = mask.getpixel((x, y))
        # modified_pixel = tuple([min(int(factor_norm*(x*(1+m/255)) if m > 150 else factor_black*(x*(1+m/255))), 255)
        #                        for x in i] if m else i)
        modified_pixel = tuple([min(int(factor_norm*(x*(1+m/255))), 255)
                                for x in i] if m else i)
        img.putpixel((x, y), modified_pixel)

img.show()
