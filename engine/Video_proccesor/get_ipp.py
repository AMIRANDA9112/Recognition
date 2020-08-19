import cv2
from engine.Detection_proccesor.person_detection import person_detection
import time


def get_ipp(ip, size, detail):
    size = int(size) / 10
    detail = int(detail) / 10

    ip = "https://" + ip
    capture = cv2.VideoCapture(ip)

    cap = cv2.VideoCapture(0)

    cap.set(5, 3)

    ret, frame = capture.read()

    back_frame = frame

    while True:

        ret, frame = capture.read()

        if frame is not None:

            cv2.resize(frame, (0, 0), fx=size, fy=size)
            n = person_detection(frame, detail)
            back_frame = frame
            cv2.imshow('Ip Pedestrian Analysis', n)

            if cv2.waitKey(1) == 27:
                break

        else:
            cv2.imshow('Fail Ip connection', back_frame)

            if cv2.waitKey(1) == 27:
                break

    capture.release()

    cv2.destroyAllWindows()
