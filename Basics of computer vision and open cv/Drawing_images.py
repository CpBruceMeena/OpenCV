import cv2
import numpy as np

#Creating a black image all zeros turn it into a black image
image = np.zeros((512, 512, 3), np.uint8)

image_bw = np.zeros((512, 512), np.uint8)

cv2.imshow("image", image)
cv2.imshow("image_bw", image_bw)

#Creating a line
#cv2.line(image, starting coordinate, end coordinate, color, thickness)
cv2.line(image, (0, 0), (512, 512), (123, 23, 53), 4)

#Creating a rectangle
# -1 is used to fill the rectangle and any other number will denote the thickness
cv2.rectangle(image, (56, 123), (435, 358), (126, 196, 214), -1)

#creating a circle
#cv2.circle(image, center, radius, color, then the thickness or -1 to fill the circle)
cv2.circle(image, (325,52), 100, (135, 63, 182), -1)

#to write text on the image
# 75 290 is the bottom left starting coordinates of the text
cv2.putText(image, "hello world", (75, 290), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170, 0), 3)

cv2.imshow("drawing Picture", image)

#It will show the window until the user press a key
cv2.waitKey(0)

#This closes all windows
cv2.destroyAllWindows()

