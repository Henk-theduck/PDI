import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('morphological_car.png')

topHat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT, kernel)
blackHat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT, kernel)

img2 = cv2.morphologyEx(topHat,cv2.MORPH_BLACKHAT, kernel)
img3 = cv2.morphologyEx(blackHat,cv2.MORPH_TOPHAT, kernel)

plt.subplot(221), plt.imshow(img)
plt.title('Original')
# plt.subplot(222), plt.imshow(img2)
# plt.title('Top Hat => Black Hat')
plt.subplot(222), plt.imshow(img3)
plt.title('Black Hat => Top Hat')
# plt.subplot(222), plt.imshow(topHat)
# plt.title('Top Hat')
plt.subplot(223), plt.imshow(blackHat)
plt.title('Black Hat')

plt.tight_layout()
plt.show()