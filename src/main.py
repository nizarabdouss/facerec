import os
import sys
import cv2
import face_recognition as FR
import numpy as np
from simple_facerec import SimpleFacerec
from PIL import Image as im
import collect
import time
import getFace
import verification as v

#Encode Known faces
sfr = SimpleFacerec()
sfr.load_encoding_images("src/faces/")
#Load camera
cap =  cv2.VideoCapture(0)


while True:
    ret, frame  = cap.read()

    #detect faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    new_frame = getFace.FaceExtract(frame).get_frames()
    for faces in new_frame:
        x1, y1, x2, y2 = faces[0], faces[1], faces[2]+faces[0], faces[3]+faces[1]
        currFace = frame[y1:y1 + x2-x1, x1:x1 + y2-y1]
        verify = v.Verify(currFace).get_existance()
        print(verify)
        if not verify:
            print(1)
            temp = collect.Person(currFace)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)
    

    """
    for face_loc, name in zip(face_locations, face_names):
        y1 , x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        if name == "Unknown":
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            cv2.putText(frame, "Retreiving...", (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            temp = collect.Person(frame)
            '''
            print(type(frame))
            temp = collect.Person(frame) 
            print(temp.get_name(), temp.date_recorded())
            temp.create_person()
            data = im.fromarray(frame)
            data.save(f'faces/face.jpeg')
            img = cv2.imread(f'faces/face.jpeg')
            data = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            data = im.fromarray(data)
            data.save(f'faces/face.jpeg')
            os.execv(sys.argv[0], sys.argv)
            '''
        else:
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)
        """
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()