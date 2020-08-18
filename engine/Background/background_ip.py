import cv2
import numpy as np
from engine.Background.resize_b import resize_b


def background_ip(ip, dir_video, detail):
    size = int(detail) / 10
    ip = "https://" + ip
    capture = cv2.VideoCapture(ip)
    b_video = cv2.VideoCapture(dir_video)
    success, ref_img = capture.read()
    flag = 0

    while True:

        success, img = capture.read()
        cv2.resize(img, (0, 0), fx=size, fy=size)
        success2, bg = b_video.read()
        bg = resize_b(bg, ref_img)
        if flag == 0:
            ref_img = img
        # create a mask
        diff1 = cv2.subtract(img, ref_img)
        diff2 = cv2.subtract(ref_img, img)
        diff = diff1 + diff2
        diff[abs(diff) < 13.0] = 0
        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) < 10] = 0

        fgmask = gray.astype(np.uint8)
        fgmask[fgmask > 0] = 255

        fgmask_inv = cv2.bitwise_not(fgmask)

        fgimg = cv2.bitwise_and(img, img, mask=fgmask)
        bgimg = cv2.bitwise_and(bg, bg, mask=fgmask_inv)
        # combine both the BG and the FG images
        dst = cv2.add(bgimg, fgimg)
        cv2.imshow('Background Replace', dst)
        key = cv2.waitKey(5) & 0xFF
        if 27 == key:
            break
        elif ord(' ') == key:
            flag = 1

        elif ord('r') == key:
            flag = 0

    cv2.destroyAllWindows()
    capture.release()
