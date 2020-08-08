import numpy as np
import cv2
import matplotlib.pyplot as plt


def get_collage(frames, detail):
    """

    :rtype: path of video to analyze
    """

    limit_1 = int(detail) / 3
    limit_1 = limit_1
    limit_15 = int(detail) / 3
    limit_15 = limit_15
    limit_25 = (int(detail) / 3) * 2
    limit_25 = limit_25
    limit_2 = ((int(detail) / 3) * 2) - 1
    limit_2 = limit_2
    detail = int(detail) - 1
    detail = detail

    row1 = np.concatenate(frames[0:limit_1], axis=1)
    row2 = np.concatenate(frames[limit_15:limit_2], axis=1)
    row3 = np.concatenate(frames[limit_25:detail], axis=1)

    print(row3)
    collage = np.concatenate((row1, row2, row3), axis=0)
    collage = cv2.cvtColor(collage, cv2.COLOR_BGR2RGB)
    plt.imshow(collage)

    return collage
