#median filter

import cv2
import numpy as np
img=cv2.imread("../images/cocktail.jpg",0)
img=cv2.resize(img,(500,600))
result=img.copy()
height,width=img.shape

for x in range(height):
    for y in range(width):
        pix=list()
        m=x-1
        n=y-1
        add=0
        for i in range(m,m+3):
            for j in range(n,n+3):
                if i<0 or i>=height or j<0 or j>=width:
                    pix.append(0)
                else:
                    pix.append(img[i,j])

        pix.sort()
        med=pix[4]
        result[x,y]=med

final=np.hstack((img,result))
cv2.imshow("Median Filtering",final)
cv2.waitKey(0)

#alternatively
mblur=cv2.medianBlur(img,3)
cv2.imshow("Median filter",mblur)
cv2.waitKey(0)
