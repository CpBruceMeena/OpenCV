import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/latest-gaming.jpg')

#taking the B G R value of the pixel located at 0, 0
B, G, R = image[52, 12]  #this one is a colored image 
print(B, G, R)

#Cnverting to gray_image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Always remember that the gray_image has 2 dimension
print(gray_image.shape)

#this print statement will give you only one value unlike the other RGB value
#because gray_scale image has only one value that is of the intensity of the black(inshort grey)
print(gray_image[35, 23])


cv2.waitKey()
cv2.destroyAllWindows()