#Thresholding Binarization and Adaptive Thresholding
"""
Thresholding is the act of converting an image to binary form

cv2.threshold(image, Threshold value, max value, threshold type)

threshold type:
    cv2.THRESH_BINARY
    cv2.THRESH_BINARY_INV
    cv2.THRESH_TRUNC
    cv2.THRESH_TOZERO
    cv2.THRESH_TOZERO_INV
    
NOTE: Image need to be converted to greyscale before thresholding    
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg', 0)
cv2.imshow("original", image)

#values below 127 goes to a 0(black, and everything above goes to 255(white))
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh1)

#values below 127 go to 255 and values above 127 go to 0 (reverse of above)
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", thresh2)

#Values above 127 are truncated (held) at 127 (the 255 argument is unused)
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("Threshold truncated image", thresh3)

#Values below 127 go to 0, above 127 are unchanged
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("Threshold To Zero", thresh4)

ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Threshold TO ZERO ", thresh5)

cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

