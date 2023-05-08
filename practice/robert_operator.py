#robert operator

import cv2
import numpy as np
img=cv2.imread("../images/flower3.jpg",0)
img=cv2.resize(img,(500,400))
cv2.imshow("Original image",img)

maskx=np.array([[1,0],[0,-1]])
masky=np.array([[0,1],[-1,0]])

robertx=cv2.filter2D(img,-1,maskx)
roberty=cv2.filter2D(img,-1,masky)
robert=cv2.add(robertx,roberty)
cv2.imshow("Robert operator",robert)
cv2.waitKey(5000)
