#Conver Hull
"""
Any polygon which has hollowness, dent or extended vertices cannot be convex. A convex curve forms the boundary of a convex set.
Given a set of points in the plane.
the convex hull of the set is the smallest convex polygon that contains all the points of it
"""
import numpy as np
import cv2

image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/convex_hull.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)
cv2.waitKey(0)

#Threshold image
ret, thresh = cv2.threshold(gray, 176, 255, 0)

#Find contours
extra, contours, heirarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#Sort contours by area and then remove the largest frame contour(it the bydefault the full image)
n = len(contours) - 1
contours = sorted(contours, key = cv2.contourArea, reverse = False)[:n]
print(len(contours))
#Iterate through contours and draw the convex Hull
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
    cv2.imshow("Convex Hull", image)

cv2.waitKey(0)
cv2.destroyAllWindows()