"""
While uploading images always try to upload images whose size is low
means the dimension is low, because currently we are working on pixel basisx
so for large sized images our method may not work properly
especially in cases where we have to look out for particular element in the images
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/dice.png')

#To display the image
#the first paramter takes the title of window and second the name of the loaded image
cv2.imshow("First Image",image)

#It prints the shape of the image (height, width, dimension)
print(image.shape)

#Saving images which we have edited in opencv
#Takes two arguments first is the name given to the output image and the second is the image chosed to save
#the format of the saved window can be changes for .jpg to .png extension
cv2.imwrite("output.jpg", image)

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

