import face_recognition as fr
import cv2
import numpy as np
from engine.Face_proccesor.get_faces import get_faces


def classify_face(im, tags):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param tags: img
    :param im: video
    :return: list of face names
    """

    if im:

        faces = get_faces(tags)
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())

        img = cv2.resize(im, (0, 0), fx=0.5, fy=0.5)

        face_locations = fr.face_locations(img)

        if face_locations:

            unknown_face_encodings = fr.face_encodings(img, face_locations)

            face_names = []
            for face_encoding in unknown_face_encodings:
                # See if the face is a match for the known face(s)
                matches = fr.compare_faces(faces_encoded, face_encoding)
                name = "Unknown"

                # use the known face with the smallest distance to the new face
                face_distances = fr.face_distance(faces_encoded, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # Draw a box around the face
                    cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 255, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 255, 255), cv2.FILLED)
                    font = cv2.QT_FONT_LIGHT
                    cv2.putText(img, name, (left - 20, bottom + 15), font, 1.0, (0, 0, 0), 2)

                return img
            else:
                pass
    else:
        return "fail"