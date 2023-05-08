#average of two images into a single image

import cv2
img1=cv2.imread("../images/flower.jpg")
img1=cv2.resize(img1,(400,500))
img2=cv2.imread("../images/flower2.jpg")
img2=cv2.resize(img2,(400,500))
img3=(img1+img2)/2
cv2.imshow("Average image",img3)
cv2.waitKey(0)
