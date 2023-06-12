#filter laplacian
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gambar2.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgaja = cv2.GaussianBlur(gray,(3,3),0)
laplacian = cv2.Laplacian(imgaja,cv2.CV_64F)

plt.subplot(1,2,1)
plt.imshow(imgaja, cmap='gray')
plt.title('Original')   
plt.xticks([])
plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.xticks([])
plt.yticks([])
plt.show()
#atau
img = cv2.imread('gambar2.jpeg',0)
blur = cv2.GaussianBlur(img,(3,3),0)
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian1 = laplacian/laplacian.max()
cv2.imshow('laplacian-gaussian', laplacian1)
cv2.waitKey(0)
