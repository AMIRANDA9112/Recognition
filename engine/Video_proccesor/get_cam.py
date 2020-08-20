import cv2
from engine.Detection_proccesor.get_faces import get_faces
from engine.Detection_proccesor.classify_face import classify_face


def get_cam(dir_faces):
    faces = get_faces(dir_faces)
    capture = cv2.VideoCapture(0)

    ret, frame = capture.read()

    back_frame = frame

    while True:

        ret, frame = capture.read()

        if frame is not None:

            n = classify_face(frame, faces)

            cv2.imshow('WebCam Face Analysis', n)

            back_frame = frame

            if cv2.waitKey(1) == 27:
                break
        else:
            cv2.imshow('Fail WebCam connection', back_frame)

            if cv2.waitKey(1) == 27:
                break

    capture.release()

    cv2.destroyAllWindows()
