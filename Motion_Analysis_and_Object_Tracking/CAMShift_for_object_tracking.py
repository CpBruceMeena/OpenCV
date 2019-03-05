# -*- coding: utf-8 -*-
"""
Camshift - An object tracking algorithm
It is very similar to meanshif, however you may have noted the window in meanshit is of fixed size
That is problematic since movement in images can be small or large. If the window is too large, you 
can miss the object when tracking.
Camshift uses an adaptive window size that changes both size and orientation.
We'll simply apply it. The steps are:
    1. Applies Meanshift till it converges.
    2. Calculates the size of the window
    3. Calculates the orientation by using the best fitting ellipse
"""

import cv2
import numpy as np

#Initialize Web Cam
cap = cv2.VideoCapture(0)

#take first frame of the video
ret, frame = cap.read()

#Setup default location of the window
r, h, c, w = 240, 100, 400, 160
track_window = (c, r, w, h)

#Crop region of interest for tracking
roi = frame[r:r+h, c:c+w]

#Convert cropped window to HSV color space
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

#define lower blue and upper blue
lower_blue = np.array([105, 0, 0])
upper_blue = np.array([125, 255, 255])
mask = cv2.inRange(hsv_roi, lower_blue, upper_blue)

#Obtain the color histogram of the ROI
#CalcHist is simply a function that calculates the color histogram for an array of images
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

#Normalize values to lie between the range 0, 255.
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

#Setup the termination criteria
#We stop calculating the centroid shift after ten iteration
#or if the centroid has moved at least 1 pixel
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    
    #Read webcam image
    ret, frame = cap.read()
    
    if ret == True:
        #Convert image from RGB to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #Calculate the histogram back projection
        #Each pixel's value is it's probability
        #calcBlackProject is a somewhat more complicated function, that calculates the histogram back projection.
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        #Apply camshift to get the location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        #Draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, 255, 2)
        
        img2 = cv2.flip(img2, 1)
        cv2.imshow("meanshift image", img2)
    
        if cv2.waitKey(1)== 13:
            break

cap.release()
#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()


