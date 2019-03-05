"""
Backgrond Subtraction:
    It allows us to separate foregrounds from the backgrounds in a video stream.
There are various types of inbuilt background subtraction methods predefined in openCV.
1. Gaussian Mixure-based Background/Foreground Segmentation Algorithm.

"""

import numpy as np
import cv2

#for taking the video from user
cap = cv2.VideoCapture("C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/pedestrian.mp4")

#Using WebCam
#cap = cv2.VideoCapture(0)

foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    
    #Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)
    
    cv2.imshow("Output", foreground_mask)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()