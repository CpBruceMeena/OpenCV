#Line Detection - Hough Lines and Probabilistic Hough Lines
"""
p = xcox(theta)+ysin(theta)
p is the perpendicular distance from origin
theta is the angle formed by the normal of this line to the origin
(measured in radians)

cv2.HoughLines(binarized image, p accuracy, theta accuracy, threshold)

Probabilistic:
cv2.HoughLinesP(binarized image, p accuracy, theta accuracy, threshold, minimum line length, max line gap)
-Threshold here is the minimum vote for it to be considered a line
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/Lines.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

""" 
Run HoughLines using a rho accuracy of 1 pixel theta accuracy of np.pi/180
which is 1 degree. Our line threshold is set to 240 (number of points on line)"""

print("For Hough Lines")

lines = cv2.HoughLines(edges, 1, np.pi/180, 240)

#We iterate through each line and convert it to the format
#required by cv lines (i.e. requiring end points)
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

cv2.imshow("hough line", image)
cv2.waitKey(0)

Pimage= cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/Lines.png')

cv2.imshow("Probability Image", Pimage)
cv2.waitKey(0)

gray = cv2.cvtColor(Pimage, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)


lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200, 5, 1)
print(lines.shape)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(Pimage, (x1,y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("Probabilistic Solution", Pimage)

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

