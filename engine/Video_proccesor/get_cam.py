import cv2
from engine.Face_proccesor.get_faces import get_faces
from engine.Face_proccesor.classify_face import classify_face


def get_cam(dir_faces):
    faces = get_faces(dir_faces)
    capture = cv2.VideoCapture(0)

    while True:

        ret, frame = capture.read()
        n = classify_face(frame, faces)

        cv2.imshow('video original', n)

        if cv2.waitKey(1) == 27:
            break

    capture.release()

    cv2.destroyAllWindows()
