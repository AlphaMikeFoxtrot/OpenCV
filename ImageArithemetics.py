import cv2
import numpy as np

img = cv2.imread('mainlogo.png')

rows, cols, channels = img.shape
roi_img = img[0:rows, 0:cols]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(gray, 100, 150
                          , cv2.THRESH_BINARY_INV)

cv2.imshow('treshold', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
