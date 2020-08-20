import cv2


def resize_b(video_b, img):
    width = img.shape[1]
    height = img.shape[0]
    lim = (width, height)
    resized = cv2.resize(video_b, lim, interpolation=cv2.INTER_AREA)
    return resized
