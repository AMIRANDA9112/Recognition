import cv2
from engine.Video_proccesor.get_frames import get_frames
from engine.Face_proccesor.classify_face import classify_face


def compile_video(dir, faces, detail=0.5):
    """

    :rtype: path of video to analyze
    """
    if dir.endswith(".mp4"):

        dir_video = dir

        video = cv2.VideoCapture(dir_video)
        count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()

        detail = detail * 100

        frames = []
        counter = 0
        for f in get_frames(dir_video):
            if counter != 0:
                if counter % detail == 0:
                    n = classify_face(f, faces)
                    frames.append(n)
            counter += 1

        for f in get_frames(frames):
            if f is None:
                break
            cv2.imshow('Match', f)
            if cv2.waitKey(10) == 27:
                break
        cv2.destroyAllWindows()

    else:
        "fail"
