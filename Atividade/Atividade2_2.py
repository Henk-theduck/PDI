import cv2 as cv
import numpy as np

gray = cv.imread('macaco.jpg', cv.IMREAD_GRAYSCALE)

cv.imshow('gray', gray)

row, col = gray.shape
for x in range(1,row-2,+3):
    for y in range(1,col-2,+3):
        gray[x,y] = ((int(gray[x-1,y-1])+int(gray[x,y-1])+int(gray[x+1,y-1])+
                      int(gray[x-1,y])+int(gray[x,y])+int(gray[x+1,y])+
                      int(gray[x-1,y+1])+int(gray[x,y+1])+int(gray[x+1,y+1])) / 9)
        gray[x-1,y-1] = gray[x,y]
        gray[x,y-1] = gray[x,y]
        gray[x+1,y-1] = gray[x,y]
        gray[x-1,y] = gray[x,y]
        gray[x+1,y] = gray[x,y]
        gray[x-1,y+1] = gray[x,y]
        gray[x,y+1] = gray[x,y]
        gray[x+1,y+1] = gray[x,y]
        
        
cv.imshow('reduzido', gray)

cv.waitKey(0)
cv.destroyAllWindows()