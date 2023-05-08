#Color separation into R,G and B from a color image

import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("../images/tiger.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Original Image",img)

b,g,r=cv2.split(img)
zero=np.zeros_like(b)
blue=cv2.merge([b,zero,zero])
green=cv2.merge([zero,g,zero])
red=cv2.merge([zero,zero,g])

cv2.imshow("Blue image",blue)
cv2.waitKey(0)
cv2.imshow("Red image",red)
cv2.waitKey(0)
cv2.imshow("Green image",green)
cv2.waitKey(0)
