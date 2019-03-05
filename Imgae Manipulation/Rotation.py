import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

cv2.imshow("original image", image)
height, width = image.shape[:2]

#Divide by two to rotate the image around its center
#cv2.getRotationMatrix2D(rotation center x, rotation center y, angle of rotation (anticlockwise), scale)
rotation_matrix =  cv2.getRotationMatrix2D((width/2, height/2), 45, 0.6)

#Don't forget to warpAffine the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("rotated image", rotated_image)

#we can also use transpose(img)
rotated_image_transpose = cv2.transpose(image) 

cv2.imshow("using_transpose", rotated_image_transpose)
#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

#WarpAffine means we can do transpose, rotatino, scaling means the paralled lines are lines are paralled after and before transformation
#The other version is called Non_Affine which, in this the paralled lines will change