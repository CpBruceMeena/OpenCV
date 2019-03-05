# -*- coding: utf-8 -*-
"""
Getting Perspective Transform
We are actuall trying to get a piece from an image and then converting it 
into a single straight affine image which in the earlier case was non affine image
We are working on a particular piece and extracting information from it
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

cv2.imshow("Original", image)
cv2.waitKey(0)

#Coordinates of the 4 coordinates of the rectangle than we want to select from the image
points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

#Coordinates of the 4 coordinates of the desired output
#We use a ratio of an A4 paper 
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

M = cv2.getPerspectiveTransform(points_A, points_B)

warped = cv2.warpPerspective(image, M, (420, 594))

cv2.imshow("warpPerspective", warped)
#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

"""
In case of affine transform we need only 3 coordinates
In affine transformation, the parallelismis maintained
while in case of non affine transform its not.
"""