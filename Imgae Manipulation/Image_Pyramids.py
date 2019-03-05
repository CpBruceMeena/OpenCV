#Pyramiding image refers to either upscaling and downscaling the image

#This comes in useful when making object detectors that scale images each time it looks for an object

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow("Original", image)
cv2.imshow("smaller", smaller)
cv2.imshow("larger", larger)

#Upscaling from smaller image to larger will make it blurrey compared to original one 

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

