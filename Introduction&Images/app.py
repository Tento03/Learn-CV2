import cv2

img=cv2.imread('op.jpg',1)
img=cv2.resize(img,(400,400))
new_img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('tes.jpg',new_img)
cv2.imshow('img',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()