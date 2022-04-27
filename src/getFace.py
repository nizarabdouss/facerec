import cv2
import numpy as np
from PIL import Image as im

class FaceExtract():
    def __init__(self, frame: np.ndarray):
        self._frame = frame
        self._newframes = self.get_face()
    
    def get_face(self) -> list[tuple]:
        face = []
        gray = cv2.cvtColor(self._frame, cv2.cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
        for (x, y, w, h) in faces:
            eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
            face.append(([x, y, w, h], self.get_eyes(gray)))
        return face

    def get_frames(self):
        return self._newframes

    def get_eyes(self, gray) -> list[tuple]:
        eye_loc = []
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(self._frame ,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eye_loc.append()
        
