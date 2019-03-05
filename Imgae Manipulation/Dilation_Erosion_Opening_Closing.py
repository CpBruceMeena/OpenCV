"""
Dilation = Adds pixel to the boundaries of objects in an image
Erosion = Remove pixels at the boundaries of objects in an image
Opening = Erosion followed by dilation
Closing = Dilation followed by erosion

When using dilation the pixels are added means the image will become brighter
When using erosion the pixels are removed means the image will become darker
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

#Defining kernel size
kernel = np.ones((5, 5), np.uint8)

#Erosion
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow("Erosion", erosion)
cv2.waitKey()

#Dilation
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow("Dilation", dilation)

#Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)
cv2.waitKey()

#Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

