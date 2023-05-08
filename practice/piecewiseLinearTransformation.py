#piecewise linear transformation (contrast stretching)

import cv2

img=cv2.imread("../images/flower.jpg")
img=cv2.resize(img,(500,600))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",img)   
h,w=img.shape

r1,r2=1,255
s1,s2=1,130
for i in range(h):
    for j in range(w):
        if img[i,j]>0 and img[i,j]<=r1:
            img[i,j]=(s1/r1)*img[i,j]
        elif img[i,j]>r1 and img[i,j]<=r2:
            img[i,j]=((s2-s1)/(r2-r1)*(img[i,j]-r1))+s1
        else:
            img[i,j]=((255-s2)/(255-r2))+(img[i,j]-r2+s2)
                 
cv2.imshow("Stretched image",img)
cv2.waitKey(0)
