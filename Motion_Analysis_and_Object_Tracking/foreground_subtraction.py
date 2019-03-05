"""
Foreground Subtraction
"""

import numpy as np
import cv2

#Using WebCam
cap = cv2.VideoCapture(0)

#Storing the first frame
ret, frame = cap.read()

#Create a float numpy array with frame values
average = np.float32(frame)

while True:

    #Get webcam frame
    ret, frame = cap.read()

    #It looks at movement in the image
    #It accumulate the weight for the things that aren't moving
    #0.01 is the weight of image, play around to see how it changes
    cv2.accumulateWeighted(frame, average, 0.01)
    
    #Scales calculates absolute values, and converts the result to 8-bit
    background = cv2.convertScaleAbs(average)
    
    cv2.imshow("Input ", frame)
    cv2.imshow("Disappearing Background ", background)
    
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()