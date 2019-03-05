#Arithmetic operations brightening and darkening images

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

M = np.ones(image.shape, dtype = 'uint8')*75

# to add the matrix M to image
#Adding will increase the brightness
added = cv2.add(image, M)
cv2.imshow("added image", added)

#to subtract the matrix M from subtract
#Subtracting will decrease the brightness and will move towards the darkness
subtract = cv2.subtract(image, M)
cv2.imshow("subtracted image", subtract)
#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

