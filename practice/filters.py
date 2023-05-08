#various types of filtering
import cv2
import numpy as np
img=cv2.imread("../images/flower3.jpg")
img=cv2.resize(img,(500,400))
cv2.imshow("Original image",img)
cv2.waitKey(5000)
kernel=np.ones((5,5),np.float32)/25

#box filer or mean filter
hblur=cv2.filter2D(img,-1,kernel)
cv2.imshow("mean filter",hblur)
cv2.waitKey(5000)

#gauss filter
gblur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Gaussian Filter",gblur)
cv2.waitKey(5000)

#median filter
mblur=cv2.medianBlur(img,5)
cv2.imshow("Median filter",mblur)
cv2.waitKey(5000)

#average filter
ablur=cv2.blur(img,(5,5))
cv2.imshow("Average filter",ablur)
cv2.waitKey(5000)

#bilateral filter
bblur=cv2.bilateralFilter(img,9,70,80)
cv2.imshow("Bilateral filter",bblur)
cv2.waitKey(5000)
