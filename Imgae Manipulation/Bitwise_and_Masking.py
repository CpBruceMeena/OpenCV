#Bitwise Operations and Masking

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

#this creates a black image window
square = np.zeros((300, 300), np.uint8)

#this creates a rectangle in that square
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey(0)

#this create an image with name ellipse
ellipse = np.zeros((300, 300), np.uint8)

#This creates a ellipse in that window named ellipse
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("ellipse", ellipse)
cv2.waitKey()

#bitwise means using and or and xor for taking binary operation
#It works in the same way as it works between 0 and 1
#we are actually performing operations between binary ellipse and binary square
#First we are taking and operation between ellipse and square

And = cv2.bitwise_and(square, ellipse)
cv2.imshow("And", And)
cv2.waitKey()

#Now we are taking or operation 
Or = cv2.bitwise_or(square, ellipse)
cv2.imshow("Or", Or)
cv2.waitKey()
 
#XOR operation
XOR = cv2.bitwise_xor(square, ellipse)
cv2.imshow("XOr", XOR)
cv2.waitKey()

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

