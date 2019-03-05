"""
Blob Detection
Blobs can be described as groups of connected pixels that all share a common property
"""
import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/blob.jpg', 0)
cv2.imshow("image", image)
#Set up the detector with default parameters
detector = cv2.SimpleBlobDetector_create()

#Detect blobs
keypoints = detector.detect(image)

#Draw detected blobs as red circles,
#cv2.DRAW_MATCHES_FLAGS_
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blobs", blobs)

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

