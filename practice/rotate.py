#rotate image in cloclwise and anti-clockwise direction

import cv2
img=cv2.imread("../images/balloon.jpg")
img=cv2.resize(img,(600,500))
h,w,_=img.shape
cx,cy=h/2,w/2

m1=cv2.getRotationMatrix2D((cx,cy),50,1)
rotated=cv2.warpAffine(img,m1,(w,h))
cv2.imshow("Rotated image" ,rotated)
cv2.waitKey(0)

m1=cv2.getRotationMatrix2D((cx,cy),50,-1)
rotated=cv2.warpAffine(img,m1,(w,h))
cv2.imshow("Rotated image" ,rotated)
cv2.waitKey(0)
