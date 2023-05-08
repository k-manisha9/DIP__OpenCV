#sobel operator

import cv2
import numpy as np
img=cv2.imread("../images/flower3.jpg",0)
img=cv2.resize(img,(500,400))
cv2.imshow("Original image",img)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
sobel=cv2.add(sobelx,sobely)
cv2.imshow("Sobel operator",sobel)
cv2.waitKey(5000)


#alternatively

maskx=np.array([[-2,-4,-2],[0,0,0],[2,4,2]])
masky=np.array([[-2,0,2],[-4,0,4],[-2,0,2]])

sobelx=cv2.filter2D(img,-1,maskx)
sobely=cv2.filter2D(img,-1,masky)
sobel=cv2.add(sobelx,sobely)
cv2.imshow("Sobel operator",sobel)
cv2.waitKey(5000)
