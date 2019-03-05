"""
Meanshift = An object Tracking Algorithm
Its premise is simple, it tracks objects by finding the maximun density of a discrete sample of points and then recalculates it at the next frame.
This effectively, moves our observation window in the direction the object has moved.
"""

import cv2
import numpy as np

#to load an image 
image = cv2.imread('C:/Users/LENOVO IDEAPAD 320/OneDrive/Desktop/Python_Projects/CV2 Learning Codes/Required Images/dice.png')

#It will show the window until the user press a key
cv2.waitKey(0)

#when you have seen all the windows press ESC at the last to destroy all the windows
#the waitKey(0) means it is waiting for ESC key
#waitKey(1) == 13 means press ENTER
#This closes all windows
cv2.destroyAllWindows()

