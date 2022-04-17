from re import I
import cv2
import numpy as np

#Ficou borrado e a imagem cortada

img = cv2.imread('ifma-caxias.jpg')

rows,cols = img.shape[:2]

def draw_circle(event,x,y,flags,param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,[0,255,0],-1)
        mouseX, mouseY = x, y

def rotate(center, angle):
    M = cv2.getRotationMatrix2D(center,angle,1)
    # cos = np.abs(M[0,0])
    # sin = np.abs(M[0,1])

    # nCols = int((rows * sin) + (cols * cos))
    # nRows = int((rows * cos) + (cols * sin))

    # M[0,2]+=((nCols)/2.0) - center[0]
    # M[1,2]+=((nRows)/2.0) - center[1]


    res = cv2.warpAffine(img, M,(cols,rows))
    return res

cv2.namedWindow('Rotate')
cv2.setMouseCallback('Rotate', draw_circle)

angle = 0

while(1):
    cv2.imshow('Rotate', img)
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key == ord('r'):
        img = rotate((mouseX,mouseY), angle+15)
cv2.destroyAllWindows()        
