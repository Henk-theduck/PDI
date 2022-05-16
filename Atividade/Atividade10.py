import numpy as np
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('ifmalogo.png')
imglogo = cv2.imread('ifmalogo.png')
mask = cv2.imread('masklogo.png', 0)

rows, cols = mask.shape[0:2]
imgCrop = img[0:rows, 0:cols]

ns = cv2.inpaint(imgCrop,mask,3,cv2.INPAINT_NS)

img[0:rows, 0:cols] = ns


cv2.imshow('Original',imglogo)
# cv2.imshow('Mask',mask)
# cv2.imshow('ns',ns)
cv2.imshow('sem logo',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(221), plt.imshow(imglogo)
# plt.title('ImagemLogo')
# plt.subplot(222), plt.imshow(mask, 'gray')
# plt.title('Máscara')
# plt.subplot(223), plt.imshow(ns)
# plt.title('NS')
# plt.subplot(224), plt.imshow(img)
# plt.title('Imagem')

# plt.tight_layout()
# plt.show()