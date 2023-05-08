#histogram equalization of a gray image

import cv2
import matplotlib.pyplot as plt
img=cv2.imread("../images/balloon.jpg")
img=cv2.resize(img,(600,500))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",img)   
hist=cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.xlim(0,256)
plt.title("Historam of a gray image")
plt.show()

new_img=cv2.equalizeHist(img)       
cv2.imshow("Equalized image",new_img)
cv2.waitKey(0)
hist=cv2.calcHist([new_img],[0],None,[256],[0,256])

plt.plot(hist)
plt.xlim(0,256)
plt.title("Historam equalization of a gray image")
plt.show()

