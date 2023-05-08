#mean filter

import cv2
import numpy as np
img=cv2.imread("../images/cocktail.jpg",0)
img=cv2.resize(img,(500,600))
result=img.copy()
height,width=img.shape

for x in range(height):
    for y in range(width):
        m=x-1
        n=y-1
        add=0
        for i in range(m,m+3):
            for j in range(n,n+3):
                if i<0 or i>=height or j<0 or j>=width:
                    add+=0
                else:
                    add+=img[i,j]

        avg=add//9
        result[x,y]=avg

final=np.hstack((img,result))
cv2.imshow("Mean Filtering",final)
cv2.waitKey(0)

#alternatively
kernel=np.ones((3,3),np.float32)/25
hblur=cv2.filter2D(img,-1,kernel)
cv2.imshow("Mean filtering",hblur)
cv2.waitKey(0)
