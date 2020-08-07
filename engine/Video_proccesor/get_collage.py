import numpy as np
import cv2
from engine.Video_proccesor.get_frames import get_frames


def get_collage(dir, detail=15):
    """

    :rtype: path of video to analyze
    """
    if dir.endswith(".mp4"):

        dir_video = dir

        video = cv2.VideoCapture(dir_video)
        count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()

        skip_frames = count // detail

        frames = []
        counter = 0
        for f in get_frames(dir_video):
            if counter != 0:
                if (counter % skip_frames) == 0:
                    frames.append(f)
            counter += 1

        limit_1 = int(detail / 3) - 1
        limit_2 = (int(detail / 3) * 2) - 1
        detail = int(detail) - 1
        print(len(frames))
        print(frames[0:5])
        row1 = np.concatenate(frames[0:4], axis=1)

        print(frames[5:10])
        row2 = np.concatenate(frames[5:9], axis=1)

        print(frames[10:14])
        row3 = np.concatenate(frames[10:14], axis=1)

        print(row3)
        collage = np.concatenate((row1, row2, row3), axis=0)
        collage = cv2.cvtColor(collage, cv2.COLOR_BGR2RGB)

        return collage

    else:
        return ValueError
