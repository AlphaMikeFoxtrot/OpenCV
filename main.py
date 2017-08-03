##############################################################################################################
## TO ALI:                                                                                                  ##
## ENTER THE FOLLOWING COMMANDS IN YOUR LINUX TERMINAL:                                                     ##                
##      1. pip install cv2 (if this command returns an error, try this command : pip2 install cv2)          ##
##      2. pip install numpy                                                                                ##                                                           
##      3. pip install matplotlib                                                                           ##
##                                                                                                          ##
## AFTER ALL THE PACKAGES HAVE BEEN SUCCESFULLY INSTALLED, cd INTO THE DIR YOU HAVE DOWNLOADED MY FILES IN. ##
## THEN TYPE IN THE FOLLOWING :                                                                             ##
##      "python main.py"                                                                                    ##
##      immedietly look into your webcam(without specs, ofcourse)                                           ##
##      then call me!                                                                                       ##
##############################################################################################################


##    Stump-based 20x20 frontal eye detector.
##    Created by ANONYMOUS (http://umich.edu/~shameem)
##
##////////////////////////////////////////////////////////////////////////////////////////
##
##  IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING.
##
##  By downloading, copying, installing or using the software you agree to this license.
##  If you do not agree to this license, do not download, install,
##  copy or use the software.
##
##
##                        Intel License Agreement
##                For Open Source Computer Vision Library
##
## Copyright (C) 2000, Intel Corporation, all rights reserved.
## Third party copyrights are property of their respective owners.
##
## Redistribution and use in source and binary forms, with or without modification,
## are permitted provided that the following conditions are met:
##
##   * Redistribution's of source code must retain the above copyright notice,
##     this list of conditions and the following disclaimer.
##
##   * Redistribution's in binary form must reproduce the above copyright notice,
##     this list of conditions and the following disclaimer in the documentation
##     and/or other materials provided with the distribution.
##
##   * The name of Intel Corporation may not be used to endorse or promote products
##     derived from this software without specific prior written permission.
##
## This software is provided by the copyright holders and contributors "as is" and
## any express or implied warranties, including, but not limited to, the implied
## warranties of merchantability and fitness for a particular purpose are disclaimed.
## In no event shall the Intel Corporation or contributors be liable for any direct,
## indirect, incidental, special, exemplary, or consequential damages
## (including, but not limited to, procurement of substitute goods or services;
## loss of use, data, or profits; or business interruption) however caused
## and on any theory of liability, whether in contract, strict liability,
## or tort (including negligence or otherwise) arising in any way out of
## the use of this software, even if advised of the possibility of such damage.

## THIS IS A SMALL PROJECT THAT SHOWS HOW FACE RECOGNITION WORKS IN PYTHON USING
## HAAR CASCADE PHP

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
s, img = cap.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h). Once we get these locations, we can create a ROI for the face and apply eye detection on this ROI (since eyes are always on the face !!! ).

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    cv2.imshow('face', roi_color)
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)


cv2.release()
##cv2.imshow('original', gray)
##cv2.waitKey(0)
cv2.destroyAllWindows()

