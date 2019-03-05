#Convolutions and Blurring
#A Convolution is a mathematical opertion performed on two functions producing a third function which is typically a modified version of one of the original functions

#In computer vision we use kernel's to specify the size over which we run our manipulating
#function over our image

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')
cv2.imshow("Original Image", image)
cv2.waitKey()

#Creating a kernel 3*3
kernel_3 = np.ones((3, 3), np.float32)/9

#We use cv2.filter2D to convolute the kernal with an image
blurred = cv2.filter2D(image, -1, kernel_3)
cv2.imshow("3*3 Kernel Image", blurred)
cv2.waitKey()

#Creting a kernel_7
kernel_7 = np.ones((7, 7), np.float32)/49

blurred_2 = cv2.filter2D(image, -1, kernel_7)
cv2.imshow("7*7 kernel image", blurred_2)

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

