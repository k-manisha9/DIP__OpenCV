#Grey level slicing

import cv2
import numpy as np
img=cv2.imread("../images/flower2.jpg",0)
img=cv2.resize(img,(600,500))
cv2.imshow("Original image",img)
h,w=img.shape
img_bg=img.copy()
thresh1=120
thresh2=150
##with background
for i in range(h):
    for j in range(w):
        if img[i,j]>=thresh1 and img[i,j]<=thresh2:
            img_bg[i,j]=255
        else:
            img_bg[i,j]=img[i,j]

cv2.imshow("With background",img_bg)
##without background
for i in range(h):
    for j in range(w):
        if img[i,j]>=thresh1 and img[i,j]<=thresh2:
            img_bg[i,j]=255
        else:
            img_bg[i,j]=0

cv2.imshow("Without background",img_bg)
cv2.waitKey(0)
