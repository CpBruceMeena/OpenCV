#Interpolation is used to change the original size of the image
#We can increase the width and height of the image
#There are almost 5 types of interpolation 
#INTER_AREA, INTER_CUBIC, INTER_NEAREST, INTER_LANCZOS4, INTER_LINEAR

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

#cv2.resize(image, dsize(output, imagesize), xscale, yscale, interpolation)
#changing the image to 3/4th of its size
image_scale = cv2.resize(image, None, fx = 0.75, fy = 0.75)
cv2.imshow("Scaling - Linear Transformatio", image_scale)
cv2.waitKey(0)

#Applying the INTERCUBIC interpolation
img_scale = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Scaling - Cubic Interpolation", img_scale)                
cv2.waitKey(0)

#Applying the INTER AREA interpolation
img_area = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow("INTER AREA IMAGE", img_area)

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

