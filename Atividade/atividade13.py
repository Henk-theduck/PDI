import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('classificadores/haarcascade_eye.xml')

capture = cv2.VideoCapture(0)

if(not capture.isOpened()):
    print('Erro ao exibir video')
else:
    while capture.isOpened():
        _, img = capture.read()
        gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)# 1.3, 5
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                cv2.imshow('Video', img)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()