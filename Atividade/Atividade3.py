import cv2
import numpy as np

img = cv2.imread("logo-if.jpg")

def func_brilho(img, br):
    brilho=[br,br,br]
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum(np.minimum(img[y,x]+brilho,[255,255,255]),[0,0,0])
    return res

def func_negativo(img):
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum([255,255,255]-img[y,x],[0,0,0])
    return res

def func_contraste(img, ct):
    contraste = [ct,ct,ct]
    res=np.zeros(img.shape, np.uint8)
    for y in range(0,img.shape[0]):
        for x in range(0,img.shape[1]):
            res[y, x] = np.maximum(np.minimum(img[y,x]*contraste,[255,255,255]),[0,0,0])
    return res

cv2.namedWindow('Atividade-3')
brilho=0
contraste = 1
negative = False
result = img
cv2.imshow('Atividade-3', result)

while(True):
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key == ord('a'):
        brilho=min(brilho+50,255)
        result = func_brilho(img, brilho)
        cv2.imshow('Atividade-3', result)
        print('+brilho', brilho)
    elif key == ord('z'):
        brilho=max(brilho-50,-255)
        result = func_brilho(img, brilho)
        cv2.imshow('Atividade-3', result)
        print('-brilho', brilho)
    elif key == ord('n'):
        negative = not negative
        result = func_negativo(result)
        cv2.imshow('Atividade-3', result)
        print('Negativo', negative)
    elif key == ord('s'):
        contraste=min(contraste+0.2, 2.0)
        result = func_contraste(img, contraste)
        cv2.imshow('Atividade-3', result)
        print('+Contraste', contraste)
    elif key == ord('x'):
        contraste=max(contraste-0.2,0)
        result = func_contraste(img, contraste)
        cv2.imshow('Atividade-3', result)
        print('-Contraste', contraste)

cv2.destroyAllWindows()