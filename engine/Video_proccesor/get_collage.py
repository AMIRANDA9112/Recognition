import numpy as np
import cv2
from engine.Video_proccesor.get_frames import get_frames



def get_collage(dir):
    """

    :rtype: object
    """
    if dir.endswith(".mp4"):

        dirvideo = dir

        for f in get_frames(dirvideo):
            if f is None:
                break
            cv2.imshow('frame', f)
            if cv2.waitKey(10) == 27:
                break

            else:
                continue

        cv2.destroyAllWindows()

        video = cv2.VideoCapture(dirvideo)
        count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()

        skip_frames = count // 15

        frames = []
        counter = 0
        for f in get_frames(dirvideo):
            if counter != 0:
                if (counter % skip_frames) == 0:
                    frames.append(f)
            counter += 1

        row1 = np.concatenate(frames[0:5], axis=1)
        row2 = np.concatenate(frames[5:10], axis=1)
        row3 = np.concatenate(frames[10:15], axis=1)
        collage = np.concatenate((row1, row2, row3), axis=0)
        collage = cv2.cvtColor(collage, cv2.COLOR_BGR2RGB)

        return collage

    else:
        return ValueError
