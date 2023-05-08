#histogram equalization of a color image

import cv2
import matplotlib.pyplot as plt
img=cv2.imread("../images/balloon.jpg")
img=cv2.resize(img,(600,500))
cv2.imshow("Original Image",img)   
hist=cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.xlim(0,256)
plt.title("Historam of a color image")
plt.show()

b,g,r=cv2.split(img)
blue=cv2.equalizeHist(b)
green=cv2.equalizeHist(g)
red=cv2.equalizeHist(r)

new_img=cv2.merge((blue,green,red))
cv2.imshow("Equalized image",new_img)
cv2.waitKey(0)
hist=cv2.calcHist([new_img],[0],None,[256],[0,256])

plt.plot(hist)
plt.xlim(0,256)
plt.title("Historam equalization of a color image")
plt.show()

