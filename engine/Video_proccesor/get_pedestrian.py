import cv2
from engine.Detection_proccesor.person_detection import person_detection


def get_pedestrian(detail):
    capture = cv2.VideoCapture(0)

    detail = int(detail) / 10

    while True:

        ret, frame = capture.read()

        n = person_detection(frame, detail)

        cv2.imshow('video original', n)

        if cv2.waitKey(1) == 27:
            break

    capture.release()

    cv2.destroyAllWindows()
