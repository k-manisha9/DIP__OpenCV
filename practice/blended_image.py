#blending of images into a single image
import cv2
import numpy as np
img1=cv2.imread("../images/flower.jpg")
img1=cv2.resize(img1,(400,500))
img2=cv2.imread("../images/flower2.jpg")
img2=cv2.resize(img2,(400,500))
weightedSum=cv2.addWeighted(img1,0.5,img2,0.5,50)
result=np.hstack((img1,img2))
cv2.imshow("original images",result)
cv2.imshow("blended image",weightedSum)
cv2.waitKey(0)
