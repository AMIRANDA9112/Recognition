import cv2
from engine.Video_proccesor.get_frames import get_frames
from engine.Face_proccesor.classify_face import classify_face
from engine.Video_proccesor.get_collage import get_collage


def compile_video(dir_video, dir_faces, detail):
    """

    :rtype: path of video to analyze
    """

    if dir_video.endswith(".mp4"):

        video = cv2.VideoCapture(dir_video)
        count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()

        print(count)

        frames = []
        counter_append = 0
        counter = 0
        for f in get_frames(dir_video):
            if counter != 0:
                if (counter * detail) % 10 == 0:
                    n = classify_face(f, dir_faces)
                    print(counter)
                    frames.append(n)
                    counter_append += 1
                    
            counter += 1
            
        counter_append = int(counter_append)

        collage = get_collage(frames, counter_append)
        dir_v = (dir_faces + '/analyze.png')
        analyzed = cv2.imwrite(dir_v, collage)
        analyzed.release()

        return count

    else:
        "fail"
