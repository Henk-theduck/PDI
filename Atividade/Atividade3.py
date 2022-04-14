import cv2
from cv2 import imread 
import numpy as np

img = cv2.imread("logo-if.jpg")

row, col = img.shape[0:2]

def FuncBrilho():
    br = [brilho, brilho, brilho]
    output = np.zeros([row,col],np.uint8)

cv2.imshow('Logo iF',img)

cv2.waitKey(0)
cv2.destroyAllWindows()