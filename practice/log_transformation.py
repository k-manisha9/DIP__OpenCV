#log transformation
'''
c=255/log(1+max(img))  <-- dynamic

c=1  <-- static

formula:
    s=c*log(1+r)    , where s is the output pixel and r is the output pixel

'''

import cv2
import numpy as np

img=cv2.imread("../images/flower.jpg")
img=cv2.resize(img,(500,600))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
h,w=img.shape

c=255/(np.log(1+np.max(img)))

for i in range(h):
    for j in range(w):
        img[i,j]=c *(np.log(1+img[i,j]))
        
cv2.imshow("transformed image",img)
cv2.waitKey(0)
