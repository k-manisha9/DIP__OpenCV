#power law transformation or gamma transformation
'''
formula:
    s=c*r^gamma    , where s is the output pixel and r is the output pixel

'''

import cv2
import numpy as np

img=cv2.imread("../images/flower.jpg")
img=cv2.resize(img,(500,600))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gamma=2
values=np.arange(0,256)
lt=np.uint8(255*np.power((values/255.0),gamma))
result=cv2.LUT(img,lt)

cv2.imshow("Original Image",img)       
cv2.imshow("transformed image",result)
cv2.waitKey(0)
