"""
Meanshift = An object Tracking Algorithm
Its premise is simple, it tracks objects by finding the maximun density of a discrete sample of points and then recalculates it at the next frame.
This effectively, moves our observation window in the direction the object has moved.
"""

import cv2
import numpy as np

#Initialize Web Cam
cap = cv2.VideoCapture(0)

#take first frame of the video
ret, frame = cap.read()

print(type(frame))

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
        
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        #Draw it on image
        x, y, w, h = track_window
        img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        
        #to use flip, define it just above the imshow command because after flipping it 
        # it will appear on the screen, you don't need to define in the beginning.
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

