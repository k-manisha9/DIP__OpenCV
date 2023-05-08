import cv2

image=cv2.imread("../images/camera.jpg",0)
image=cv2.resize(image,(400,500))
h,w=image.shape
cx,cy=h/2,w/2
for angle in range(0,270,30):
    m=cv2.getRotationMatrix2D((cx,cy),(angle),-1)
    dst=cv2.warpAffine(image,m,(h,w))
    cv2.imshow("Rotate",dst)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    
