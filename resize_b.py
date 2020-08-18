import numpy as np


def resize_b(video_b, img):
    height, width = img.shape
    lim = (width, height)
    resized = cv2.resize(video_b, lim, interpolation=cv2.INTER_AREA)
    return resized
