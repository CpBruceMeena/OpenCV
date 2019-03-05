#Sharpening
#Sharpening is the opposite of Blurring, it strengths or emphasizing edges in an image

#If the kernel matrix sums to one, so there is no need to normalize
#(i.e. multiply by a factor to retain the same brightness of the original)

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')
cv2.imshow("Original Image", image)

#We don't need to normalize since the matrix sums up to one
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])

#applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow("image sharpening", sharpened) 

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

