#edge detection using laplacian operator

import cv2
import numpy as np
img=cv2.imread("../images/flower3.jpg",0)
img=cv2.resize(img,(500,400))
cv2.imshow("Original image",img)

ret,thresh=cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
edge=cv2.Laplacian(thresh,cv2.CV_8U,-1)
cv2.imshow("Edge detection using Laplacian operator",edge)
cv2.waitKey(5000)
