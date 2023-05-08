#histogram of a gray image and display it

import cv2
import matplotlib.pyplot as plt

img=cv2.imread("../images/tiger.jpg",0)
cv2.imshow("Image",img)

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.xlim([0,256])
plt.title("Histogram of a gray image")
plt.show()
