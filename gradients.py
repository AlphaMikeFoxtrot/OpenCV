import numpy as np
import cv2
def getFromVid():
    cap = cv2.VideoCapture(0)

    while True:

        _, frame = cap.read()

        sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
        sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

        edges = cv2.Canny(frame, 100, 200)

        cv2.imshow('original', frame)
        cv2.imshow('sobel', sobelx)
        cv2.imshow('sobely', sobely)
        cv2.imshow('edges', edges)

        k = cv2.waitKey(5)
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()

def getFromImg():
    img = cv2.imread('lines.jpg')

    edges = cv2.Canny(img, 100, 200)

    cv2.imshow('edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    getFromImg()

if __name__ == "__main__":
    main()
