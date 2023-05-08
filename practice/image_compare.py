#compare two images

import cv2
import numpy as np
img1=cv2.imread("../images/flower2.jpg")
img2=cv2.imread("../images/flower3.jpg")
img1=cv2.resize(img1,(600,500))
img2=cv2.resize(img2,(600,500))
cv2.imshow("First image",img1)
cv2.imshow("Second image",img2)
difference=cv2.subtract(img1,img2)
cv2.imshow("Resultant image *",difference)
cv2.waitKey(0)
b,g,r=cv2.split(difference)
if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("Both the images are equal..")
else:
    print("Images are not equal..")



