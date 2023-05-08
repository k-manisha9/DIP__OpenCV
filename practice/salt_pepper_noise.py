#salt and pepper noise

import cv2
import numpy as np
import random
image=cv2.imread("../images/balloon.jpg")
image=cv2.resize(image,(848,565))
img1=image.copy()
cv2.imshow("Original image",image)
cv2.waitKey(0)
h,w,_=image.shape
pepper=0.05
salt=0.95
for i in range(h):
    for j in range(w):
        y=random.random()
        if y<pepper:
            img1[i,j]=[0,0,0]
        elif y>salt:
            img1[i,j]=[255,255,255]
        else:
            img1[i,j]=image[i,j]

cv2.imshow("Salt and pepper noise",img1)
cv2.waitKey(0)

