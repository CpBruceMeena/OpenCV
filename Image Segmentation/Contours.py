"""
Segmentation and Contours
Segmentation = Partitioning images into different regions
Contours = They are continours lines or curves that bound or cover the full boundary of an object in an image..
Grayscale is a main step in contours
The variable contours are stored as a numpy array of (x,y) points that form the contours
While Heirarchy describes the child-parent relationship between contours

Approximation Methods
Using cv2.CHAIN_APPROX_NONE stores all the boundary points. 
using cv2.CHAIN_APPROX_SIMPLE instead only provides these start and end points of bounding contours.

Hierarchy Types 
cv2.RETR_LIST = Retrives all contours
cv2.RETR_EXTERNAL = Retrives external or outer contours only(Try to use this one)
cv2.RETR_COMP = Retrives all in a 2-level hierarchy
cv2.RETR_TREE = Retrives all in a full hierarchy
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/dice.png')
cv2.imshow("original image", image)
cv2.waitKey(0)

#Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow("edged image", edged)
cv2.waitKey(0)

#Finding Contours
#findcontours actually alters the image
#cv2.findContours(edged, Retrieval mode, Approximation method)
extra, contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("Canny edges after contouring", edged)
cv2.waitKey(0)

print("Numbers of contours found = "+ str(len(contours)))

#Draw all contours
#Use -1 as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow("Contours", image)

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

