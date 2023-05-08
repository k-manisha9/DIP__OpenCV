#join two images in such a way that the left part of first image merges with the right part of second image

import cv2
import numpy as np
img1=cv2.imread("../images/tom.jpg")
img2=cv2.imread("../images/jerry.png")
img1=cv2.resize(img1,(256,256))
img2=cv2.resize(img2,(256,256))
img3=np.hstack((img1[:,0:128],img2[:,128:256]))
cv2.imshow("first image",img1[:,0:128])
cv2.imshow("second image",img2[:,128:256])
cv2.imshow("Resultant iimage",img3)
cv2.waitKey(5000)
