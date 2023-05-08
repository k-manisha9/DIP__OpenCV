#difference operator- canny operator

import cv2
import numpy as np
img=cv2.imread("../images/flower3.jpg",0)
img=cv2.resize(img,(500,400))
cv2.imshow("Original image",img)
canny=cv2.Canny(img,100,200)
cv2.imshow("Canny edge detector",canny)
cv2.waitKey(5000)
