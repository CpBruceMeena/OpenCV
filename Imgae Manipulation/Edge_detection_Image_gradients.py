"""
Edge detection and Image Gradients
Edges can be defined as sudden changes(discontinuities ) in an image and they can encode just as much 
information as pixels
Here Image Gradients mean derivative

There are three types of Edge Detection:
    Sobel: to emphasize vertical or horizontal edges
    Laplacian: Gets all orientations
    Canny: Optimal due to low error rate, well defined edges and accurate detection
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg',0)
   
height, width = image.shape

#Extract Sobel Edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 5) 

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.imshow("Sobel X", sobel_x)
cv2.waitKey(0)
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("Sobel OR", sobel_OR)
cv2.waitKey() 


laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("Laplacian", laplacian)
cv2.waitKey(0)

#Canny edge detection uses gradient values as thresholds
"""
Then we need to provide two thresholds values: threshold 1 and threshold2.Any gradient value larger than threshold2 is considered to be an edge.
Any value below threshold 1 is considered not to be an edge.
Values in between threshold1 and threshold2 are either classified as edges or non-edges based on how their
intensities are connected.  
"""

canny = cv2.Canny(image, 20, 170)
cv2.imshow("Canny", canny)

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

