import cv2
import numpy as np

img = cv2.imread('visiting_card2.jfif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## detecting corners
corners = cv2.goodFeaturesToTrack(gray, 4, 0.05, 70)
corners = np.float32(corners)

## drawing circles representing the corners
for corner in corners:
    x, y = corner[0]
    cv2.circle(img, (x,y), 5, 255, -1)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
