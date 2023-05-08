# brightness enhancement of an image

import cv2
import numpy as np

img = cv2.imread("../images/flower2.jpg")
img = cv2.resize(img, (600, 500))
alpha = 2
beta = 0
gamma = 50
enhanced = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), beta, gamma)
cv2.imshow("Original image", img)
cv2.imshow("Enhanced image", enhanced)
cv2.waitKey(0)
