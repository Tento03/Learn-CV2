import cv2
import numpy as np

img=cv2.imread('assets/soccer_practice.jpg',0)
template=cv2.imread('assets/ball.PNG',0)
h,w=template.shape


# cv2.TM_CCOEFF:Metode ini menghitung perbedaan antara template dan rata-rata nilainya dibandingkan dengan bagian gambar yang lebih besar.
# TM_CCOEFF_NORMED lebih tahan terhadap variasi pencahayaan dan intensitas dalam gambar karena hasilnya lebih seragam dan tidak tergantung pada ukuran template.
# Cross-Correlation mengukur kesamaan antara template dan bagian gambar. Ini menghitung hasil perkalian antara nilai piksel template dan gambar pada posisi tertentu.
# Versi normalisasi dari TM_CCORR. Dengan normalisasi, nilai pencocokan berkisar antara 0 dan 1, di mana 1 menunjukkan kecocokan sempurna.
# Metode ini bekerja dengan baik untuk gambar dengan kesamaan intensitas antara template dan gambar utama.

# Sum of Squared Differences (SSD) menghitung perbedaan kuadrat antara template dan bagian gambar pada setiap posisi.
#  berfungsi baik untuk gambar yang tidak memiliki perbedaan intensitas antara template dan gambar utama.
# Norm:Digunakan ketika template dan gambar utama memiliki intensitas yang sangat mirip, karena metode ini sangat sensitif terhadap perubahan.
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result=cv2.matchTemplate(img2,template,method)
    print(result)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
