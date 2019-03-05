"""
SIFT SURF FAST BRIEF and ORB

We are basically trying to figure out the number of keypoints
in an image and then we'll use them for object detection purpose
"""

#Important point
#this error : Incorrect type of self:
#It is because of the version of opencv that we are using, so while creating detector use _create at the last.

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/blob.jpg')

#Using SIFT:
"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT()

keypoints = sift.detector(gray, None)
print("Number of keypoints detected : " , len(keypoints))

image1 = cv2.drawKeypoints(image , keypoints, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Image SIFT", image1)
"""

#Using SURF
"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
surf = cv2.SURF()

surf.hessianThreshold = 7500
keypoints, descriptors = surf.detectAndCompute(gray, None)
print("Number of keypoints detected : " , len(keypoints))

image1 = cv2.drawKeypoints(image , keypoints, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Image SURF", image1)
""" 

#this is for the FAST Method
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fast = cv2.FastFeatureDetector_create()

keypoints = fast.detect(gray, None)
print("Number of keypoints detected : " , len(keypoints))

#Use the None as the third parameter otherwise it will not function well
image1 = cv2.drawKeypoints(image, keypoints, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Image FAST", image1)
cv2.waitKey(0)


"""
#Using Brief Method
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Create fast detector object
fast = cv2.FastFeatureDetector_create()

#Create brief detector object
brief = cv2.xfeatures2d.SIFT_create()

#Determine key points
keypoints = fast.detect(gray, None)
print("Number of keypoints detected : " , len(keypoints))

#Obtain descriptors and new final keypoints using BRIEF
keypoints, descriptors = brief.compute(gray, keypoints)
print("Number of keypoints found", len(keypoints))

#Use the None as the third parameter otherwise it will not function well
image2 = cv2.drawKeypoints(image, keypoints, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Image BRIEF", image2)
"""

#Using ORB method

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(100)

keypoints = orb.detect(gray, None)

keypoints, descriptors = orb.compute(gray, keypoints)
print("Number of keypoints detected : " , len(keypoints))

#Use the None as the third parameter otherwise it will not function well
image2 = cv2.drawKeypoints(image, keypoints, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Image ORB", image2)



cv2.waitKey(0)



#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()