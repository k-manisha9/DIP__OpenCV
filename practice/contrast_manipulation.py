#contrast manipulation of an image

import cv2
import numpy as np
img=cv2.imread("../images/flower2.jpg")
img=cv2.resize(img,(600,500))
new_img=cv2.convertScaleAbs(img,5,3)
cv2.imshow("Original image",img)
cv2.imshow("Enhanced image",new_img)
cv2.waitKey(0)
