import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

#getting the height and width of the image
height, width = image.shape[:2]

#taking the amount of shift to be done to the image
quarter_height = height/4
quarter_width = width/4

#we need to write the translation matrix
#      [1 0 | Tx ]
# T = [0 1 | Ty ] , T is the translation matrix
T = np.float32([[1, 0, quarter_width], [0 , 1, quarter_height]])

#using warpAffine function to carry out the translation
img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translated Image',img_translation)

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

