import cv2

img=cv2.imread('assets/op.jpg', 1)
newimg=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
newimg2=cv2.resize(img,(300,400),fx=0.5,fy=0.5)

cv2.imshow('Display Image',newimg2)
# cv2.imshow('Tes Img',newimg)
key=cv2.waitKey(0)

if key==ord('Q') or key==ord('q'):
    cv2.imwrite('assets/Tes.jpg', img)

cv2.destroyAllWindows()