import face_recognition as fr
import cv2
import numpy as np


def classify_face(im, faces):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param faces: faces
    :param im: video
    :return: list of face names
    """
    if im is not None:
        if im.any():

            faces_encoded = list(faces.values())
            known_face_names = list(faces.keys())
            img = im

            face_loc = fr.face_locations(img)

            if face_loc:

                unknown_face_encodings = fr.face_encodings(img, face_loc)

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

                    for (top, right, bottom, left), name in zip(face_loc, face_names):
                        # Draw a box around the face
                        cv2.rectangle(img, (left - 20, top - 20),
                                      (right + 20, bottom + 20),
                                      (255, 255, 255), 2)

                        # Draw a label with a name below the face
                        cv2.rectangle(img, (left - 20, bottom - 15),
                                      (right + 20, bottom + 20),
                                      (255, 255, 255), cv2.FILLED)

                        font = cv2.FONT_HERSHEY_COMPLEX
                        cv2.putText(img, name, (left - 20, bottom + 15),
                                    font, 1.0, (0, 0, 0), 2)
                    return img

            else:
                return img
        else:
            return "fail"
    else:
        return "fail"
