# Câu 6(3 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau.
# a. thực hiện phép xói mòn ảnh erosion.
# b. thực hiện phép giãn nở ảnh dilation.
# c. thực hiện phép mở ảnh opening.
# d. thực hiện phép đóng ảnh closing.
# e. hiện thị ảnh ban đầu , các ảnh kết quả trên matplotlib.

#cau:6
import cv2
import numpy as np
import matplotlib.pyplot as plt

anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)
blur = cv2.blur(anhxam,(5,5))

kernel = np.ones((5,5),np.uint8)

erode = cv2.erode(blur,kernel)       
dilate = cv2.dilate(blur,kernel)       
opening = cv2.morphologyEx(blur,2,kernel)  
closing = cv2.morphologyEx(blur,3,kernel)  

plt.gray()
plt.subplot(241); plt.imshow(cv2.cvtColor(anh,4));  
plt.subplot(242); plt.imshow(cv2.cvtColor(erode,4));   
plt.subplot(243); plt.imshow(cv2.cvtColor(dilate,4));  
plt.subplot(244); plt.imshow(cv2.cvtColor(opening,4)); 
plt.subplot(245); plt.imshow(cv2.cvtColor(closing,4)); 
plt.show()