import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('assets/chessboard.png')
img=cv2.resize(img,(0,0),fx=0.75,fy=0.75)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# max corners:jumlah titik yg akan ditampilkan
# quality level:kualitas minimum sudut
# min distance:jarak antar titik
corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners=np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # Lingkaran merah pada gambar berwarna

cv2.imshow('display',img)
cv2.waitKey(0)
cv2.destroyAllWindows()