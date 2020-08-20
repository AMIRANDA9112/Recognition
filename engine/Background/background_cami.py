import cv2
import numpy as np
from engine.Background.resize_b import resize_b


def background_cami(dir_img):
    video = cv2.VideoCapture(0)
    success, ref_img = video.read()
    bg = cv2.imread(dir_img)
    back_frame = ref_img

    flag = 0
    while True:
        success, img = video.read()
        bg = resize_b(bg, ref_img)
        if img is not None and bg is not None:

            back_frame = img

            if flag == 0:
                ref_img = img
            # create a mask
            diff1 = cv2.subtract(img, ref_img)
            diff2 = cv2.subtract(ref_img, img)
            diff = diff1 + diff2
            diff[abs(diff) < 13.0] = 0
            gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
            gray[np.abs(gray) < 10] = 0

            fg_mask = gray.astype(np.uint8)
            fg_mask[fg_mask > 0] = 255

            fgmask_inv = cv2.bitwise_not(fg_mask)

            fg_img = cv2.bitwise_and(img, img, mask=fg_mask)
            bg_img = cv2.bitwise_and(bg, bg, mask=fgmask_inv)
            # combine both the BG and the FG images
            dst = cv2.add(bg_img, fg_img)
            cv2.imshow('Background Replace', dst)
            key = cv2.waitKey(5) & 0xFF
            if 27 == key:
                break
            elif ord(' ') == key:
                flag = 1

            elif ord('r') == key:
                flag = 0

        else:
            cv2.imshow('Fail WebCam connection', back_frame)

            if cv2.waitKey(1) == 27:
                break

    cv2.destroyAllWindows()
    video.release()
