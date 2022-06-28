import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atividade_aula11.png', 0)


kernel = np.ones((141,71), np.uint8)
kernel2 = np.ones((71,71), np.uint8)
kernel3 = np.ones((0,141), np.uint8)


imgTwo = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel, iterations= 1)
dilation = cv2.dilate(img,kernel2,iterations = 1)
erosion = cv2.erode(img,kernel3,iterations = 2)



plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(imgTwo)
plt.title('primeira')
plt.subplot(223), plt.imshow(erosion)
plt.title('segunda')
plt.subplot(224), plt.imshow(dilation)
plt.title('terceira')



plt.tight_layout()
plt.show()