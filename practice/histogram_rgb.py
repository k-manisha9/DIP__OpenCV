#histogram of an rgb image and display it

import cv2
import matplotlib.pyplot as plt

img=cv2.imread("../images/tiger.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Original Image",img)

red=cv2.calcHist([img],[0],None,[256],[0,256])
green=cv2.calcHist([img],[1],None,[256],[0,256])
blue=cv2.calcHist([img],[2],None,[256],[0,256])

plt.plot(red)
plt.xlim([0,256])
plt.title("Histogram of an RGB image: Red channel")
plt.show()

plt.plot(green)
plt.xlim([0,256])
plt.title("Histogram of an RGB image: Green channel")
plt.show()

plt.plot(blue)
plt.xlim([0,256])
plt.title("Histogram of an RGB image: Blue channel")
plt.show()
