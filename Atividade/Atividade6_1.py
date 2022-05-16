import cv2
import numpy as np

img = cv2.imread('noise.jpg')

remake = cv2.medianBlur(img,9)

cv2.imshow('Remake',remake)
cv2.imshow('original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()