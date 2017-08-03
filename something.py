import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('face2.jpg', cv2.IMREAD_GRAYSCALE)

faces = face_cascade.detectMultiScale(img, 1.3, 5)

for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_gray, (ey, ex), (ey+ew, ex+eh), (0, 255, 0), 2)

cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
