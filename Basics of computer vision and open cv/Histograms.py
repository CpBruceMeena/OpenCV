import cv2
import numpy as np
from matplotlib import pyplot as plt

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/others/latest-gaming.jpg')

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#Don't forget to write the image in the array form
#When using in the histogram it should be in second level array form
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

#We plot a histogram, ravel() flattens our image array
plt.hist(image.ravel(), 256, [0, 256])
plt.show()

#viewing separate color channels
color = ('b', 'g', 'r')

#We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0, 256])

cv2.waitKey()
cv2.destroyAllWindows()