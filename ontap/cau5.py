# Câu 5(3 điểm): Viết chương trình thực hiện các yêu cầu sau.
# a. tạo ảnh âm bản từ ảnh gốc.
# b. xoay ảnh với góc xoay nhập vào từ bàn phím quanh tâm ảnh , scale = 1.
# c. tách biên ảnh sobel cả hướng x và y.
# d. tìm contour từ ảnh tách biên , vẽ contour màu đỏ lên ảnh gốc.
# e. hiển thị ảnh gốc , âm bản , xoay , sobel , contour trên matplotlib.

import cv2
import numpy as np
import matplotlib.pyplot as plt
anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)


anhamban = 255 - anh

gocxoay = int(input('gocxoay='))
cao,rong = anh.shape[:2]
tamxoay = (rong//2,cao//2)
matranxoay = cv2.getRotationMatrix2D(tamxoay,gocxoay,1)
anhxoay = cv2.warpAffine(anh,matranxoay,(rong,cao))

gauss = cv2.GaussianBlur(anhxam,(5,5),0)
sobelx = cv2.convertScaleAbs(cv2.Sobel(gauss,6,1,0))
sobely = cv2.convertScaleAbs(cv2.Sobel(gauss,6,0,1))
abssobelx = cv2.convertScaleAbs(sobelx)
abssobely = cv2.convertScaleAbs(sobely)
anhsobel = cv2.addWeighted(abssobelx,0.5,abssobely,0.5,0)

contour,_ = cv2.findContours(anhsobel,1,2)
anhcontour = anh.copy()
cv2.drawContours(anhcontour,contour,-1,(0,0,255),2)

plt.gray()
plt.subplot(241),plt.imshow(cv2.cvtColor(anh,4))
plt.subplot(242),plt.imshow(cv2.cvtColor(anhamban,4))
plt.subplot(243),plt.imshow(cv2.cvtColor(anhxoay,4))
plt.subplot(244),plt.imshow(cv2.cvtColor(anhsobel,4))
plt.subplot(245),plt.imshow(cv2.cvtColor(anhcontour,4))
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()