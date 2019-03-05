#Sorting Contours
"""
Sorting Contours is quite useful when doing image processing
Sorting by Area can assist in Object Recognition (using contour area)
means firt the shape with largest area will be contoured and then it follows the decresing order 
  -Eliminate small contours that may be noise
  -Extract the largest contour
Sorting by spatial position(using the contour centrouid)
 -Sort characters left to right
 -Process images in specific order

"""

import cv2
import numpy as np

#Function we'll use to display contour area
def get_contour_areas(contours):
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas
    
#to load an image   
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/shapes.jpg')
original_image = image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow("edged image", edged)
cv2.waitKey(0)

extra, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


print("Contour areas before sorting")
print(get_contour_areas(contours))


sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)

print("Contour area after sorting")
print(get_contour_areas(sorted_contours))

#Iterates over our contours and draw one at a time
for c in sorted_contours:
    cv2.drawContours(original_image, [c], -1, (255, 0, 0), 3)
    cv2.waitKey(0)
    cv2.imshow("Contours by area", original_image)

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

