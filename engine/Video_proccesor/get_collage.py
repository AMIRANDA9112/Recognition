import numpy as np


def get_collage(frames, count):
    """

    :rtype: path of video to analyze
    """
    nf = int(count)

    nf = (nf // 3) * 3

    print('Making Collage,Total Frames To Collage = {}'.format(nf))

    l1 = nf / 3
    l1 = int(l1)

    l2 = (nf / 3) * 2
    l2 = int(l2)

    l3 = nf

    row1 = np.concatenate(frames[0:l1], axis=1)

    row2 = np.concatenate(frames[l1:l2], axis=1)

    row3 = np.concatenate(frames[l2:l3], axis=1)

    collage = np.concatenate((row1, row2, row3), axis=0)
    return collage
