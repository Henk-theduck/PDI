#Aplicar o algoritmo Canny em video
import cv2
import numpy as np
capture = cv2.VideoCapture('IFMA Campus Caxias.mp4')

if (not capture.isOpened()):
    print('Erro ao exibir video')
else:
    while capture.isOpened():
        _, frame = capture.read()
        frame = cv2.Canny(frame,200,200)
        cv2.imshow('Canny Video', frame)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()
#Detectar moedas
import cv2
import numpy as np

orig = cv2.imread('coins.jpeg')
res=orig.copy()
img_blur = cv2.medianBlur(orig,5)
img_blur = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,100,param1=200,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(res,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(res,(i[0],i[1]),2,(255,0,0),3)
cv2.imshow('HoughCircles',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
