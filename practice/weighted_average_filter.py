#weighted average filter

import cv2
import numpy as np
img=cv2.imread("../images/cocktail.jpg",0)
img=cv2.resize(img,(500,600))
result=img.copy()
height,width=img.shape
mask=[[1,2,3],[2,4,2],[1,2,1]]
for x in range(height):
    for y in range(width):
        pix=list()
        m=x-1
        n=y-1
        add=0
        a=0
        b=0
        for i in range(m,m+3):
            for j in range(n,n+3):
                if i<0 or i>=height or j<0 or j>=width:
                    add+=0*mask[a][b]
                else:
                    add+=img[i,j]*mask[a][b]
            b+=1
        a+=1
        avg=add//16
        result[x,y]=avg

final=np.hstack((img,result))
cv2.imshow("Weighted average Filtering",final)
cv2.waitKey(0)
