#Gaussian noise
import cv2
import numpy as np
import random
image=cv2.imread("../images/balloon.jpg")
image=cv2.resize(image,(848,565))
cv2.imshow("Original image",image)
cv2.waitKey(0)
s=image.size
h,w,c=image.shape
gauss=np.random.normal(0,1,s)
gauss=gauss.reshape(h,w,c).astype('uint8')
result=cv2.add(image,gauss)
cv2.imshow("Gaussian noise",result)
cv2.waitKey(0)
