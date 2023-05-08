#multiplication of two images

import cv2
import numpy as np
img1=cv2.imread("../images/flower2.jpg")
img2=cv2.imread("../images/flower3.jpg")
img1=cv2.resize(img1,(600,500))
img2=cv2.resize(img2,(600,500))
cv2.imshow("First image",img1)
cv2.imshow("Second image",img2)
mul=img1*img2
cv2.imshow("Multiplication using *",mul)

#alternatively
mul=cv2.multiply(img1,img2)
cv2.imshow("Multiplication using multiply()",mul)
cv2.waitKey(0)

