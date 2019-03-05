#Cropping the image
#Cropping is basically taking a certain number of the the rows and column of the image matrix
import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

height, width = image.shape[:2]

#Don't forget to convert the coordinates into integer
#Specifying the starting pixel coordinates(top left of crop rectangle)
start_row, start_col = int(height*.25) , int(width*.25)

#Specifying the ending pixel coordinates( bottom right of crop rectangle) 
end_row, end_col = int(height*.75), int(width*.75)

cropped = image[start_row : end_row, start_col : end_col]

cv2.imshow("original image", image)
cv2.waitKey(0)

cv2.imshow("Cropped Image", cropped)
#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows() 