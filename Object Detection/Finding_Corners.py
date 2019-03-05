"""
Finding Corners:
    Corners are identified when shifting a window in any direction over 
    that point gives a large change in intensity
"""
import cv2
import numpy as np
 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/chess.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.goodFeaturesToTrack(input image, maxCorners, quality level, minDistance)
corners = cv2.goodFeaturesToTrack(gray, 150, 0.01, 15)

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(image, (x-5,y-5),(x+5, y+5), (0, 255, 0), 2)

cv2.imshow("Corners Found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()