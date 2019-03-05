import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/01_13_54_web.jpg')

#converting the image to HSV image
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', hsv_image)

#this means we want all the 2 dimension values and then only hue values
cv2.imshow('Hue Image', hsv_image[:, :, 0])

#this means we want only the saturation values
cv2.imshow('Saturation Image', hsv_image[:, :, 1])

#thie means we want only the values
cv2.imshow('Value Image', hsv_image[:, :, 2])


cv2.waitKey()
cv2.destroyAllWindows()