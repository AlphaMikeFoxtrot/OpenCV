import cv2
import numpy as np


img = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
cv2.rectangle(img, (250, 250), (800, 800), (255,255,255), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
