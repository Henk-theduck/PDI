import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atividade_aula11.png')

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(img,kernel,iterations = 2)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(dilation)
plt.title('Dilation')
plt.subplot(223), plt.imshow(erosion)
plt.title('Erosion')
plt.subplot(224), plt.imshow(grad)
plt.title('Gradient')

plt.tight_layout()
plt.show()