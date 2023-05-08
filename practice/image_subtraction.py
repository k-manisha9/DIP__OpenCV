#subtraction of two images

import cv2
import numpy as np
img1=cv2.imread("../images/flower2.jpg")
img2=cv2.imread("../images/flower3.jpg")
img1=cv2.resize(img1,(600,500))
img2=cv2.resize(img2,(600,500))
cv2.imshow("First image",img1)
cv2.imshow("Second image",img2)
sub=img1-img2
cv2.imshow("Subtraction using -",sub)

#alternatively
sub=cv2.subtract(img1,img2)
cv2.imshow("Subtraction using subtract()",sub)
cv2.waitKey(0)

