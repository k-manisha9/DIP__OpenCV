#image negative

import cv2

img=cv2.imread("../images/tiger.jpg")
img=cv2.resize(img,(500,500))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Original Image",img)

negative=255-img
cv2.imshow("Negative image",negative)
cv2.waitKey(0)

#alternatively
h,w,_=img.shape
negative=img.copy()
for i in range(h):
    for j in range(w):
        negative[i,j]=255-img[i,j]
    
cv2.imshow("Negative image",negative)
cv2.waitKey(0)
