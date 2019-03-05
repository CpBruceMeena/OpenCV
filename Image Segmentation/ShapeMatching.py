#Shape Matching
"""
cv2.matchShapes(contour template, contour, method, method parameter)
output = match value(lower values, means a closed match)

 -Contour template = This is our reference countour that we're trying to find in the new image
 Contour = The individual contour we are chekcing against
 Method = Type of contour matching(1, 2, 3)
 Method Parameter = leava along as 0, 0(not fully utilized in python OpenCv)
  
"""
import cv2
import numpy as np

#to load an image 
template = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/circle.png', 0)
cv2.imshow("Template", template)
cv2.waitKey(0)

#Load our target image with the shapes we're trying to match
target = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/shapes.png')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

#Threshold both images first before using cv2.frames
ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

#find contours
extra, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

#we need to sort the contour by area so that we can remove the largest
#counter which is the image outline
sorted_contour = sorted(contours, key = cv2.contourArea, reverse = True)

print(len(contours))
template_contour = contours[1]

extra ,contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    match = cv2.matchShapes(template_contour, c, 1, 0.0)
    print(match) 
    
    #the comparison between match operator is in hit and trail manner
    if match < 0.018:
        cv2.drawContours(target, [c], -1, (0, 255, 0), 3)
        cv2.imshow("Output", target)

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

