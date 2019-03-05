#Approximating Contours and Finding their Convex Hulls
"""
cv2.approxPolyDP(contour, Approximation, Accuracy, Closed)
Approximating accuracy = Important parameter is determining the accuracy of the approximation. Small values give precise-
approximation, large values give more generic approximation. A good rule of thumn is les than 5 % of the contour perimeter
Closed = a Boolean value that states whether the appoximate contour should be open or closed.
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/hut.jpg')

orig_image = image.copy()
cv2.imshow("Original Image", orig_image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

extra, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#Iterates through each contours and compute the bounding rectangel
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(orig_image, (x,y), (x+w, y+h), (0,0,255),2)
    cv2.imshow("Bounding Rectangle", orig_image)
    cv2.waitKey(0)

#Iterate through each contour and compute the approx contour
for c in contours:
    accuracy = 0.03*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.imshow("Approx Poly DP", image)
    

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

