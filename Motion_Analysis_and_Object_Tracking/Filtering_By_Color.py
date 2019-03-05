"""
Filtering by color: From a given picture we are trying to get a particular color
and not taking into account the other colors
"""

import cv2
import numpy as np

#Initialize Web Cam
cap = cv2.VideoCapture(0)

#define lower blue and upper blue
lower_blue = np.array([105, 0, 0])
upper_blue = np.array([125, 255, 255])

while True:
    
    #Read webcam image
    ret, frame = cap.read()
    
    #Convert image from RGB to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Use inRange to capture only the values between upper blue and lower blue
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    
    #Perform bitwise AND on mask and our original frame
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("Original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Filtered color only", res)

    if cv2.waitKey(1)== 13:
        break

cap.release()
#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

