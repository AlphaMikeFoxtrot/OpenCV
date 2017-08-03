import numpy as np
import cv2

def capVid():
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    #fourcc = cv2.cv.CV_FOURCC(*'DIVX')
    #out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame0 = cap.read()
        if ret==True:
            frame = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY) 

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def editImage():
    
    img = cv2.imread('image.png',cv2.IMREAD_ANYCOLOR)
    cv2.rectangle(img, (850, 250), (1500, 1500), (0, 255, 0), 2)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    editImage()

main()
