#Gauss filter

import cv2
import numpy as np
img=cv2.imread("../images/cocktail.jpg",0)
img=cv2.resize(img,(500,600))
result=img.copy()
height,width=img.shape
gblur=cv2.GaussianBlur(img,(3,3),0)
cv2.imshow("Gaussian Filter",gblur)
cv2.waitKey(0)
