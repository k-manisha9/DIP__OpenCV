#Segment an image using thresholding technique
import cv2
import numpy as np
import random
image=cv2.imread("../images/balloon.jpg",0)
image=cv2.resize(image,(848,565))
cv2.imshow("Original image",image)
ret,thresh=cv2.threshold(image,120,255,cv2.THRESH_BINARY)
cv2.imshow("Gaussian noise",thresh)
cv2.waitKey(0)
