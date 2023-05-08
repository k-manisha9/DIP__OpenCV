# clockwise rotate 90 degree
import cv2

image=cv2.imread("../images/deer.png")
img1=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
img2=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original image",image)
cv2.imshow("Clockwise Rotation",img1)
cv2.imshow("Anti-clockwise Rotation",img2)
cv2.waitKey(0)
