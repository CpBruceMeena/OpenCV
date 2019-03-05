import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/latest-gaming.jpg')

cv2.imshow("Original Image", image)
cv2.waitKey(0)

#to convert the image to gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#there is also another method to convert it to gray image
#using the 0 at the end of the imread line 
bw_image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/latest-gaming.jpg',0)

cv2.imshow("bw_image", bw_image)

cv2.imshow("grayscale image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()