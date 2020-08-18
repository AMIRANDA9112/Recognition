from __future__ import print_function
from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2


def person_detection(frame, detail):

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = frame
    image = imutils.resize(image, width=min(400, image.shape[1]))
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=detail)
    for (xA, yA, xB, yB) in pick:

        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    return image
