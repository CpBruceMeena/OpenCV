import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

print(image.shape)
#to take all the values of image according to the B G R
B, G, R = cv2.split(image)

#this will all print the same value as the dimension of the actual image
print(B.shape)
print(G.shape)
print(R.shape)

#all this images will be grayscale because they are all one dimension
cv2.imshow("Red Image", R)
cv2.imshow("Green Image", G)
cv2.imshow("Blue Image", B)

#Lets remake the original image
#We can combine all the B G R values to get back the original image
merged = cv2.merge([B, G, R])
cv2.imshow("merge image", merged)

#printing all the red, blue, green section
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("red", cv2.merge([zeros, zeros, R]))
cv2.imshow("green", cv2.merge([zeros,G , zeros]))
cv2.imshow("blue", cv2.merge([B, zeros, zeros]))


cv2.waitKey(0)
cv2.destroyAllWindows()

#Important note
#Basically each B G R is a two dimensional matrix with a single value for each value of x and y
#when we are writing the above statement we are taking the particular R G B matrix and their values 
# and then merging them with the zeros matrix