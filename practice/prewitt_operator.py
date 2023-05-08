#prewitt operator

import cv2
import numpy as np
img=cv2.imread("../images/flower3.jpg",0)
img=cv2.resize(img,(500,400))
cv2.imshow("Original image",img)

maskx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
masky=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

prewittx=cv2.filter2D(img,-1,maskx)
prewitty=cv2.filter2D(img,-1,masky)
prewitt=cv2.addWeighted(prewittx,0.5,prewitty,0.5,0)
cv2.imshow("Prewitt operator",prewitt)
cv2.waitKey(5000)
