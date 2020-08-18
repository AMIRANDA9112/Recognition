import cv2
from engine.Detection_proccesor.get_faces import get_faces
from engine.Detection_proccesor.classify_face import classify_face


def get_ipf(ip, dir_faces, size):
    size = int(size) / 10

    faces = get_faces(dir_faces)
    ip = "https://" + ip
    capture = cv2.VideoCapture(ip)

    while True:

        ret, frame = capture.read()
        cv2.resize(frame, (0, 0), fx=size, fy=size)
        n = classify_face(frame, faces)

        cv2.imshow('Ip Faces Analysis', n)

        if cv2.waitKey(1) == 27:
            break

    capture.release()

    cv2.destroyAllWindows()
