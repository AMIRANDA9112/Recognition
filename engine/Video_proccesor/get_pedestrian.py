import cv2
from engine.Detection_proccesor.person_detection import person_detection


def get_pedestrian(detail):
    capture = cv2.VideoCapture(0)

    detail = int(detail) / 10

    back_frame = capture[1]

    while True:

        ret, frame = capture.read()

        if frame is not None:

            n = person_detection(frame, detail)

            cv2.imshow('WebCam Pedestrian Detection', n)

            back_frame = frame

            if cv2.waitKey(1) == 27:
                break

        else:
            cv2.imshow('Fail WebCam connection', back_frame)

            if cv2.waitKey(1) == 27:
                break

    capture.release()

    cv2.destroyAllWindows()
